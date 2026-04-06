"""
Web-based Walkthrough Builder for Ren'Py games.
Provides a Flask API and serves a modern React-like frontend for comparing playthroughs.
"""

import os
import re
import ast
from difflib import SequenceMatcher
from collections import Counter
from threading import Lock
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from rpy_parser import extract_game_data, CacheManager, RPyParser

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Global cache for game data
game_data = None
data_lock = Lock()
cache_manager = CacheManager()
parser = RPyParser()
SOURCE_DIRS = ['Season_1', 'Season_2']
MAX_COMPARISON_ITEMS = 250
MAX_DIFF_LINES = 2500
DIFF_CONTEXT_LINES = 3


def data_supports_scene_state_actions(data):
    """Check whether extracted scene payload includes state action metadata."""
    seasons = data.get('seasons', {})
    if not isinstance(seasons, dict):
        return False

    for scenes in seasons.values():
        if not isinstance(scenes, dict):
            continue

        for scene in scenes.values():
            if not isinstance(scene, dict):
                continue

            return 'state_actions' in scene

    return False


def data_supports_menu_branch_jump_conditions(data):
    """Check whether cached jumps include menu-option branch conditions."""
    seasons = data.get('seasons', {})
    if not isinstance(seasons, dict):
        return False

    for scenes in seasons.values():
        if not isinstance(scenes, dict):
            continue

        for scene in scenes.values():
            if not isinstance(scene, dict):
                continue

            jumps = scene.get('jumps', [])
            if not isinstance(jumps, list):
                continue

            for jump in jumps:
                if not isinstance(jump, dict):
                    continue

                conditions = jump.get('conditions', [])
                if not isinstance(conditions, list):
                    continue

                if any(str(condition or '').strip().startswith('__choice_') for condition in conditions):
                    return True

    return False


def get_game_data():
    """Load or extract game data."""
    global game_data
    if game_data is None:
        with data_lock:
            if game_data is None:
                if cache_manager.is_cache_valid(parser, SOURCE_DIRS):
                    print("Loading cached data...")
                    cached_data = cache_manager.load()
                    if (
                        cached_data is not None and
                        data_supports_scene_state_actions(cached_data) and
                        data_supports_menu_branch_jump_conditions(cached_data)
                    ):
                        game_data = cached_data
                    else:
                        print("Cache read failed or schema is stale, extracting game data...")
                        game_data = extract_game_data(SOURCE_DIRS, use_cache=False)
                else:
                    print("Extracting game data...")
                    game_data = extract_game_data(SOURCE_DIRS)
    return game_data


def dialogue_key(dialogue):
    """Build a stable key for dialogue comparison."""
    return (dialogue.get('speaker', '').strip(), dialogue.get('text', '').strip())


def normalize_choice_selections(playthrough_data):
    """Normalize choice selection payload to a key->int map."""
    raw = playthrough_data.get('choice_selections', {})
    if not isinstance(raw, dict):
        return {}

    normalized = {}
    for key, value in raw.items():
        key_text = str(key or '').strip()
        if not key_text:
            continue
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            continue
        if parsed < 0:
            continue
        normalized[key_text] = parsed

    return normalized


class SafeExpressionEvaluator(ast.NodeVisitor):
    """Evaluate a restricted subset of Python expressions for story conditions."""

    def __init__(self, variables):
        self.variables = variables

    def visit_Constant(self, node):
        return node.value

    def visit_Name(self, node):
        if node.id in self.variables:
            return self.variables[node.id]

        # Internal menu-choice markers use numeric option indices.
        # Missing values should not behave like 0 via bool/int coercion.
        if node.id.startswith('__choice_'):
            return None

        return False

    def visit_Attribute(self, node):
        parts = []
        current = node
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value

        if isinstance(current, ast.Name):
            parts.append(current.id)
            key = '.'.join(reversed(parts))
            return self.variables.get(key, False)

        raise ValueError('Unsupported attribute expression')

    def visit_List(self, node):
        return [self.visit(element) for element in node.elts]

    def visit_Tuple(self, node):
        return tuple(self.visit(element) for element in node.elts)

    def visit_Set(self, node):
        return {self.visit(element) for element in node.elts}

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            for value in node.values:
                if not bool(self.visit(value)):
                    return False
            return True

        if isinstance(node.op, ast.Or):
            for value in node.values:
                if bool(self.visit(value)):
                    return True
            return False

        raise ValueError('Unsupported bool operator')

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.Not):
            return not bool(operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError('Unsupported unary operator')

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.FloorDiv):
            return left // right
        if isinstance(node.op, ast.Mod):
            return left % right

        raise ValueError('Unsupported binary operator')

    def visit_Compare(self, node):
        left = self.visit(node.left)
        for operator, comparator_node in zip(node.ops, node.comparators):
            right = self.visit(comparator_node)

            if isinstance(operator, ast.Eq):
                ok = left == right
            elif isinstance(operator, ast.NotEq):
                ok = left != right
            elif isinstance(operator, ast.Gt):
                ok = left > right
            elif isinstance(operator, ast.GtE):
                ok = left >= right
            elif isinstance(operator, ast.Lt):
                ok = left < right
            elif isinstance(operator, ast.LtE):
                ok = left <= right
            elif isinstance(operator, ast.In):
                ok = left in right
            elif isinstance(operator, ast.NotIn):
                ok = left not in right
            elif isinstance(operator, ast.Is):
                ok = left is right
            elif isinstance(operator, ast.IsNot):
                ok = left is not right
            else:
                raise ValueError('Unsupported compare operator')

            if not ok:
                return False

            left = right

        return True

    def visit_IfExp(self, node):
        return self.visit(node.body) if bool(self.visit(node.test)) else self.visit(node.orelse)

    def visit_Call(self, node):
        raise ValueError('Calls are not supported in condition evaluation')

    def generic_visit(self, node):
        raise ValueError(f'Unsupported expression node: {type(node).__name__}')


def safe_eval_expression(expression, variable_state):
    """Safely evaluate a restricted expression against current variable state."""
    expr = str(expression or '').strip()
    if not expr:
        return False

    try:
        parsed = ast.parse(expr, mode='eval')
    except SyntaxError:
        return False

    evaluator = SafeExpressionEvaluator(variable_state)
    try:
        return evaluator.visit(parsed.body)
    except Exception:
        return False


def evaluate_condition_expression(condition, variable_state):
    """Evaluate one condition string."""
    text = str(condition or '').strip()
    if not text or text.lower() == 'else':
        return True
    return bool(safe_eval_expression(text, variable_state))


def evaluate_condition_list(conditions, variable_state):
    """Evaluate all conditions that gate a dialogue/choice option."""
    if not isinstance(conditions, list):
        return True

    for condition in conditions:
        if not evaluate_condition_expression(condition, variable_state):
            return False

    return True


def apply_choice_action(action, variable_state):
    """Apply one parsed choice action to mutable variable state."""
    if not isinstance(action, dict):
        return None

    if action.get('type') != 'assign':
        return None

    target = str(action.get('target') or '').strip()
    op = str(action.get('op') or '=').strip()
    expression = str(action.get('expression') or '').strip()
    if not target:
        return None

    rhs_value = safe_eval_expression(expression, variable_state)
    current_value = variable_state.get(target, 0)

    try:
        if op == '=':
            new_value = rhs_value
        elif op == '+=':
            new_value = current_value + rhs_value
        elif op == '-=':
            new_value = current_value - rhs_value
        elif op == '*=':
            new_value = current_value * rhs_value
        elif op == '/=':
            new_value = current_value / rhs_value
        else:
            return None
    except Exception:
        return None

    variable_state[target] = new_value
    return {
        'target': target,
        'op': op,
        'expression': expression,
        'value': new_value,
        'line_number': action.get('line_number')
    }


def materialize_playthrough(playthrough_data, data, include_dialogues=True, include_choice_states=False):
    """Expand a playthrough (scene references) into ordered dialogue lines."""
    scenes_input = playthrough_data.get('scenes', [])
    if not isinstance(scenes_input, list):
        scenes_input = []

    choice_selections = normalize_choice_selections(playthrough_data)
    variable_state = {}

    playthrough_name = (playthrough_data.get('name') or 'Unnamed Playthrough').strip()
    if not playthrough_name:
        playthrough_name = 'Unnamed Playthrough'

    collected_dialogues = []
    missing_scenes = []
    resolved_scenes = []
    selected_choices = []
    selected_option_by_choice_line = {}
    choice_states = {}
    scene_states = {}
    scene_active_by_node = {}
    scene_activation_overrides = set()

    scene_position_by_node = {}
    selected_nodes = set()
    for scene_index, scene_ref in enumerate(scenes_input, start=1):
        if not isinstance(scene_ref, dict):
            continue

        season = (scene_ref.get('season') or '').strip()
        label = (scene_ref.get('label') or '').strip()
        if not season or not label:
            continue

        scene = data.get('seasons', {}).get(season, {}).get(label)
        if scene is None:
            continue

        scene_node = (season, label)
        selected_nodes.add(scene_node)
        if scene_node not in scene_position_by_node:
            scene_position_by_node[scene_node] = scene_index

    label_to_selected_nodes = {}
    for season, label in selected_nodes:
        label_to_selected_nodes.setdefault(label, []).append((season, label))

    def resolve_jump_target_node(source_season, target_label):
        target = str(target_label or '').strip()
        if not target:
            return None

        same_season_node = (source_season, target)
        if same_season_node in selected_nodes:
            return same_season_node

        candidates = label_to_selected_nodes.get(target, [])
        if len(candidates) == 1:
            return candidates[0]

        return None

    incoming_jumps_by_target = {}
    for source_season, source_label in selected_nodes:
        source_scene = data.get('seasons', {}).get(source_season, {}).get(source_label, {})
        for jump in source_scene.get('jumps', []):
            target_node = resolve_jump_target_node(source_season, jump.get('target'))
            if not target_node:
                continue

            incoming_jumps_by_target.setdefault(target_node, []).append({
                'source': (source_season, source_label),
                'conditions': jump.get('conditions', []),
                'line_number': jump.get('line_number')
            })

    for scene_index, scene_ref in enumerate(scenes_input, start=1):
        if not isinstance(scene_ref, dict):
            continue

        season = (scene_ref.get('season') or '').strip()
        label = (scene_ref.get('label') or '').strip()
        if not season or not label:
            continue

        scene = data.get('seasons', {}).get(season, {}).get(label)
        if scene is None:
            missing_scenes.append({'season': season, 'label': label, 'scene_index': scene_index})
            continue

        scene_node = (season, label)
        incoming_candidates = incoming_jumps_by_target.get(scene_node, [])
        incoming_from_past = [
            incoming
            for incoming in incoming_candidates
            if scene_position_by_node.get(incoming['source'], 10**9) < scene_index
        ]

        if incoming_from_past:
            scene_active = any(
                scene_active_by_node.get(incoming['source'], False) and
                evaluate_condition_list(incoming.get('conditions', []), variable_state)
                for incoming in incoming_from_past
            )
        else:
            scene_active = True

        if scene_node in scene_activation_overrides:
            scene_active = True

        scene_state_key = f"{season}::{label}"
        scene_states[scene_state_key] = {
            'season': season,
            'label': label,
            'scene_index': scene_index,
            'active': scene_active,
            'incoming_jump_count': len(incoming_from_past),
            'incoming_jump_total': len(incoming_candidates)
        }

        dialogues = scene.get('dialogues', [])
        choices = scene.get('choices', [])
        state_actions = scene.get('state_actions', [])

        if isinstance(state_actions, list):
            state_actions = sorted(
                state_actions,
                key=lambda action: (
                    action.get('line_number', 10**9)
                    if isinstance(action, dict) and isinstance(action.get('line_number'), int)
                    else 10**9
                )
            )
        else:
            state_actions = []

        if isinstance(choices, list):
            choices = sorted(
                choices,
                key=lambda choice: (
                    choice.get('line_number', 10**9)
                    if isinstance(choice, dict)
                    else 10**9
                )
            )
        else:
            choices = []

        resolved_scenes.append({
            'season': season,
            'label': label,
            'scene_index': scene_index,
            'dialogue_count': len(dialogues),
            'choice_count': len(choices),
            'active': scene_active
        })

        scene_active_by_node[scene_node] = scene_active

        state_action_cursor = 0

        def apply_state_actions_until(max_line_exclusive=None):
            nonlocal state_action_cursor

            if not scene_active:
                return

            while state_action_cursor < len(state_actions):
                action = state_actions[state_action_cursor]
                state_action_line = (
                    action.get('line_number')
                    if isinstance(action, dict) and isinstance(action.get('line_number'), int)
                    else 10**9
                )

                if max_line_exclusive is not None and state_action_line >= max_line_exclusive:
                    break

                state_action_cursor += 1

                if not isinstance(action, dict):
                    continue

                if not evaluate_condition_list(action.get('conditions', []), variable_state):
                    continue

                apply_choice_action(action, variable_state)

        for choice_index, choice in enumerate(choices):
            if not isinstance(choice, dict):
                continue

            choice_line_for_order = (
                choice.get('line_number')
                if isinstance(choice.get('line_number'), int)
                else None
            )
            if choice_line_for_order is not None:
                apply_state_actions_until(choice_line_for_order)

            options = choice.get('options', [])
            if not isinstance(options, list) or len(options) == 0:
                continue

            parent_choice_line = choice.get('parent_choice_line')
            parent_option_index = choice.get('parent_option_index')
            parent_option_text = str(choice.get('parent_option_text') or '').strip()

            parent_branch_active = True
            if isinstance(parent_choice_line, int) and isinstance(parent_option_index, int):
                parent_selected_index = selected_option_by_choice_line.get(parent_choice_line)
                parent_branch_active = parent_selected_index == parent_option_index

            option_states = []
            available_indices = []
            for option_index, option in enumerate(options):
                option_active = (
                    scene_active and
                    parent_branch_active and
                    evaluate_condition_list(option.get('conditions', []), variable_state)
                )

                option_states.append({
                    'index': option_index,
                    'text': str(option.get('text') or '').strip(),
                    'line_number': option.get('line_number'),
                    'active': option_active,
                    'conditions': option.get('conditions', [])
                })

                if option_active:
                    available_indices.append(option_index)

            choice_key = f"{season}::{label}::{choice_index}"
            requested_index = choice_selections.get(choice_key)
            requested_is_valid = isinstance(requested_index, int) and 0 <= requested_index < len(options)

            if requested_is_valid and requested_index in available_indices:
                selected_index = requested_index
            elif available_indices:
                selected_index = available_indices[0]
            else:
                selected_index = None

            choice_active = parent_branch_active and bool(available_indices)
            choice_line_number = choice.get('line_number')

            if include_choice_states:
                choice_states[choice_key] = {
                    'key': choice_key,
                    'season': season,
                    'label': label,
                    'choice_index': choice_index,
                    'line_number': choice_line_number,
                    'active': choice_active,
                    'parent_branch_active': parent_branch_active,
                    'parent_choice_line': parent_choice_line,
                    'parent_option_index': parent_option_index,
                    'parent_option_text': parent_option_text,
                    'available_option_indices': available_indices,
                    'selected_option_index': selected_index,
                    'options': option_states
                }

            if selected_index is None:
                continue

            if not scene_active:
                continue

            if isinstance(choice_line_number, int):
                variable_state[f"__choice_{choice_line_number}"] = selected_index
                selected_option_by_choice_line[choice_line_number] = selected_index

            selected_option = options[selected_index]
            selected_text = str(selected_option.get('text') or '').strip()
            selected_choices.append({
                'key': choice_key,
                'season': season,
                'label': label,
                'choice_index': choice_index,
                'selected_option_index': selected_index,
                'selected_option_text': selected_text
            })

            if include_dialogues:
                collected_dialogues.append({
                    'speaker': 'Choice',
                    'text': f"{label} choice {choice_index + 1}: {selected_text}",
                    'line_number': selected_option.get('line_number'),
                    'season': season,
                    'label': label,
                    'scene_index': scene_index
                })

            for action in selected_option.get('actions', []):
                if str(action.get('type') or '').strip() == 'jump':
                    target_node = resolve_jump_target_node(season, action.get('target'))
                    if target_node:
                        scene_activation_overrides.add(target_node)
                    continue

                applied = apply_choice_action(action, variable_state)
                if not applied:
                    continue

                if include_dialogues:
                    collected_dialogues.append({
                        'speaker': 'State',
                        'text': (
                            f"{applied['target']} {applied['op']} {applied['expression']} => {applied['value']}"
                        ),
                        'line_number': applied.get('line_number'),
                        'season': season,
                        'label': label,
                        'scene_index': scene_index
                    })

        apply_state_actions_until()

        if include_dialogues and scene_active:
            for dialogue in dialogues:
                if not evaluate_condition_list(dialogue.get('conditions', []), variable_state):
                    continue

                collected_dialogues.append({
                    'speaker': dialogue.get('speaker', ''),
                    'text': dialogue.get('text', ''),
                    'line_number': dialogue.get('line_number'),
                    'season': season,
                    'label': label,
                    'scene_index': scene_index
                })

    active_scene_count = sum(1 for scene_state in scene_states.values() if scene_state.get('active'))
    inactive_scene_count = max(0, len(scene_states) - active_scene_count)

    return {
        'name': playthrough_name,
        'input_scene_count': len(scenes_input),
        'resolved_scene_count': len(resolved_scenes),
        'dialogues': collected_dialogues,
        'resolved_scenes': resolved_scenes,
        'missing_scenes': missing_scenes,
        'selected_choices': selected_choices,
        'selected_choice_count': len(selected_choices),
        'choice_states': choice_states if include_choice_states else {},
        'scene_states': scene_states,
        'active_scene_count': active_scene_count,
        'inactive_scene_count': inactive_scene_count
    }


def diff_token(dialogue):
    """Build a stable token for sequence diffing."""
    speaker = (dialogue.get('speaker') or '').strip()
    text = (dialogue.get('text') or '').strip()
    return f"{speaker}\x1f{text}"


def diff_line_payload(dialogue, position):
    """Create a payload for one line in the diff view."""
    return {
        'position': position,
        'speaker': dialogue.get('speaker', ''),
        'text': dialogue.get('text', ''),
        'season': dialogue.get('season', ''),
        'label': dialogue.get('label', ''),
        'line_number': dialogue.get('line_number'),
        'scene_index': dialogue.get('scene_index')
    }


def finalize_diff_hunk(lines):
    """Finalize hunk metadata for a list of diff lines."""
    left_positions = [line['left']['position'] for line in lines if line.get('left')]
    right_positions = [line['right']['position'] for line in lines if line.get('right')]

    left_start = left_positions[0] if left_positions else 0
    right_start = right_positions[0] if right_positions else 0
    left_count = len(left_positions)
    right_count = len(right_positions)

    header = f"@@ -{left_start},{left_count} +{right_start},{right_count} @@"

    return {
        'header': header,
        'left_start': left_start,
        'left_count': left_count,
        'right_start': right_start,
        'right_count': right_count,
        'line_count': len(lines),
        'lines': lines
    }


def build_continuous_dialogue_diff(
    left_dialogues,
    right_dialogues,
    context_lines=DIFF_CONTEXT_LINES,
    max_lines=MAX_DIFF_LINES
):
    """Build a GitHub-style diff across continuous dialogue streams."""
    left_tokens = [diff_token(dialogue) for dialogue in left_dialogues]
    right_tokens = [diff_token(dialogue) for dialogue in right_dialogues]

    left_lines = [diff_line_payload(dialogue, index + 1) for index, dialogue in enumerate(left_dialogues)]
    right_lines = [diff_line_payload(dialogue, index + 1) for index, dialogue in enumerate(right_dialogues)]

    matcher = SequenceMatcher(a=left_tokens, b=right_tokens, autojunk=False)
    opcodes = matcher.get_opcodes()

    raw_hunks = []
    pending_context = []
    current_lines = None

    added_lines = 0
    removed_lines = 0
    unchanged_lines = 0

    for tag, i1, i2, j1, j2 in opcodes:
        if tag == 'equal':
            unchanged_lines += (i2 - i1)

            equal_rows = []
            for offset in range(i2 - i1):
                equal_rows.append({
                    'type': 'context',
                    'left': left_lines[i1 + offset],
                    'right': right_lines[j1 + offset]
                })

            if current_lines is None:
                if len(equal_rows) > context_lines:
                    pending_context = equal_rows[-context_lines:]
                else:
                    pending_context = equal_rows
            else:
                if len(equal_rows) > context_lines * 2:
                    current_lines.extend(equal_rows[:context_lines])
                    raw_hunks.append(current_lines)
                    current_lines = None
                    pending_context = equal_rows[-context_lines:]
                else:
                    current_lines.extend(equal_rows)

            continue

        if tag in ('delete', 'replace'):
            removed_lines += (i2 - i1)
        if tag in ('insert', 'replace'):
            added_lines += (j2 - j1)

        if current_lines is None:
            current_lines = []
            if pending_context:
                current_lines.extend(pending_context)

        if tag in ('delete', 'replace'):
            for offset in range(i2 - i1):
                current_lines.append({
                    'type': 'remove',
                    'left': left_lines[i1 + offset],
                    'right': None
                })

        if tag in ('insert', 'replace'):
            for offset in range(j2 - j1):
                current_lines.append({
                    'type': 'add',
                    'left': None,
                    'right': right_lines[j1 + offset]
                })

        pending_context = []

    if current_lines:
        if pending_context:
            current_lines.extend(pending_context)
        raw_hunks.append(current_lines)

    trimmed_hunks = []
    remaining_lines = max_lines
    truncated = False

    for lines in raw_hunks:
        if remaining_lines <= 0:
            truncated = True
            break

        if len(lines) <= remaining_lines:
            trimmed_hunks.append(lines)
            remaining_lines -= len(lines)
            continue

        trimmed_hunks.append(lines[:remaining_lines])
        remaining_lines = 0
        truncated = True

    if len(trimmed_hunks) < len(raw_hunks):
        truncated = True

    serialized_hunks = [finalize_diff_hunk(lines) for lines in trimmed_hunks if lines]
    has_changes = any(line['type'] != 'context' for hunk in raw_hunks for line in hunk)

    return {
        'overview': {
            'left_total_lines': len(left_dialogues),
            'right_total_lines': len(right_dialogues),
            'unchanged_lines': unchanged_lines,
            'added_lines': added_lines,
            'removed_lines': removed_lines,
            'change_blocks': len(raw_hunks),
            'has_changes': has_changes,
            'similarity_ratio': round(matcher.ratio(), 4),
            'context_lines': context_lines
        },
        'hunks': serialized_hunks,
        'truncated': truncated
    }


def season_sort_key(season):
    """Sort seasons by numeric component first, then by name."""
    match = re.search(r'(\d+)', season or '')
    if match:
        return (int(match.group(1)), season)
    return (10**9, season or '')


def chapter_file_sort_key(file_path):
    """Sort chapter files semantically (e.g., Chapter3 < Chapter3.5 < Chapter4)."""
    normalized = str(file_path or '').replace('\\', '/')
    base_name = os.path.basename(normalized)
    stem = os.path.splitext(base_name)[0]
    stem_lower = stem.lower()

    # Keep generic start labels at the top of the season timeline.
    if stem_lower == 'start':
        return (0, 0, 0, 0, stem_lower)

    chapter_match = re.match(
        r'^chapter(?P<major>\d+)(?:(?:[x\.])(?P<minor>\d+))?(?P<suffix>.*)$',
        stem_lower
    )
    if chapter_match:
        major = int(chapter_match.group('major'))
        minor_raw = chapter_match.group('minor')
        minor = int(minor_raw) if minor_raw is not None else 0
        suffix = (chapter_match.group('suffix') or '').strip()
        lewd_rank = 1 if 'lewd' in suffix else 0
        return (1, major, minor, lewd_rank, stem_lower)

    # Non-chapter files are kept after canonical chapter files.
    return (2, 10**9, 10**9, 0, stem_lower)


def infer_scene_line_number(scene):
    """Estimate a scene's source line from contained items."""
    candidates = []

    for dialogue in scene.get('dialogues', []):
        line_number = dialogue.get('line_number')
        if isinstance(line_number, int):
            candidates.append(line_number)

    for choice in scene.get('choices', []):
        line_number = choice.get('line_number')
        if isinstance(line_number, int):
            candidates.append(line_number)

    for jump in scene.get('jumps', []):
        line_number = jump.get('line_number')
        if isinstance(line_number, int):
            candidates.append(line_number)

    if candidates:
        return min(candidates)

    return 10**9


def build_timeline_entries(data):
    """Build chronological timeline entries for all scenes."""
    labels = data.get('labels', {})
    seasons = data.get('seasons', {})
    entries = []

    for season, scenes in seasons.items():
        for label_name, scene in scenes.items():
            label_meta = labels.get(label_name, {})
            meta_matches = isinstance(label_meta, dict) and label_meta.get('season') == season

            file_path = str(scene.get('file_path') or '').strip()
            if not file_path and meta_matches:
                file_path = label_meta.get('file_path') or ''
            if not file_path:
                file_path = f"{season}/{label_name}.rpy"

            line_number = scene.get('label_line_number')
            if not isinstance(line_number, int) and meta_matches:
                line_number = label_meta.get('line_number')
            if not isinstance(line_number, int):
                line_number = infer_scene_line_number(scene)

            entries.append({
                'season': season,
                'label': label_name,
                'file_path': file_path,
                'line_number': line_number,
                'dialogue_count': len(scene.get('dialogues', [])),
                'choice_count': len(scene.get('choices', [])),
                'jump_count': len(scene.get('jumps', []))
            })

    entries.sort(
        key=lambda item: (
            season_sort_key(item['season']),
            chapter_file_sort_key(item.get('file_path') or ''),
            item.get('line_number', 10**9),
            item.get('label', '').lower()
        )
    )

    for index, entry in enumerate(entries, start=1):
        entry['timeline_index'] = index

    return entries


def compute_reachable_scenes(entries, data):
    """Compute reachable scenes via jump graph traversal from start labels."""
    seasons = data.get('seasons', {})
    nodes = {(entry['season'], entry['label']) for entry in entries}

    label_to_nodes = {}
    for season, label_name in nodes:
        label_to_nodes.setdefault(label_name, []).append((season, label_name))

    edges = {node: set() for node in nodes}
    for season, label_name in nodes:
        scene = seasons.get(season, {}).get(label_name, {})
        for jump in scene.get('jumps', []):
            target_label = (jump.get('target') or '').strip()
            if not target_label:
                continue

            resolved = None
            same_season_target = (season, target_label)
            if same_season_target in nodes:
                resolved = same_season_target
            else:
                candidates = label_to_nodes.get(target_label, [])
                if len(candidates) == 1:
                    resolved = candidates[0]

            if resolved:
                edges[(season, label_name)].add(resolved)

    start_nodes = [node for node in nodes if node[1].lower() == 'start']
    if not start_nodes:
        seen_seasons = set()
        for entry in entries:
            season = entry['season']
            if season not in seen_seasons:
                seen_seasons.add(season)
                start_nodes.append((entry['season'], entry['label']))

    reachable = set(start_nodes)
    queue = list(start_nodes)
    queue_index = 0
    while queue_index < len(queue):
        node = queue[queue_index]
        queue_index += 1

        for target in edges.get(node, set()):
            if target not in reachable:
                reachable.add(target)
                queue.append(target)

    return reachable


@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files."""
    return send_from_directory('static', path)


@app.route('/api/data', methods=['GET'])
def get_all_data():
    """Get all extracted game data."""
    data = get_game_data()
    return jsonify(data)


@app.route('/api/seasons', methods=['GET'])
def get_seasons():
    """Get list of available seasons."""
    data = get_game_data()
    return jsonify(list(data.get('seasons', {}).keys()))


@app.route('/api/season/<season>', methods=['GET'])
def get_season_scenes(season):
    """Get all scenes for a specific season."""
    data = get_game_data()
    if season in data.get('seasons', {}):
        return jsonify(data['seasons'][season])
    return jsonify({}), 404


@app.route('/api/scene/<season>/<label_name>', methods=['GET'])
def get_scene(season, label_name):
    """Get a specific scene's data."""
    data = get_game_data()
    if season in data.get('seasons', {}) and label_name in data['seasons'][season]:
        return jsonify(data['seasons'][season][label_name])
    return jsonify({}), 404


@app.route('/api/labels', methods=['GET'])
def get_all_labels():
    """Get all labels with their metadata."""
    data = get_game_data()
    return jsonify(data.get('labels', {}))


@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    """Get scenes in chronological order with accessibility metadata."""
    data = get_game_data()
    entries = build_timeline_entries(data)
    reachable = compute_reachable_scenes(entries, data)

    timeline = []
    for entry in entries:
        timeline.append({
            **entry,
            'reachable': (entry['season'], entry['label']) in reachable
        })

    return jsonify(timeline)


@app.route('/api/search', methods=['GET'])
def search_dialogue():
    """Search for dialogue containing specific text."""
    query = request.args.get('q', '').strip().lower()
    if not query:
        return jsonify([])
    
    data = get_game_data()
    results = []
    
    for season, scenes in data['seasons'].items():
        for label_name, scene in scenes.items():
            for dialogue in scene.get('dialogues', []):
                text = dialogue.get('text', '').lower()
                speaker = dialogue.get('speaker', '').lower()
                if query in text or query in speaker:
                    results.append({
                        'season': season,
                        'label': label_name,
                        'speaker': dialogue['speaker'],
                        'text': dialogue['text'],
                        'line_number': dialogue['line_number']
                    })
    
    return jsonify(results[:100])  # Limit to 100 results


@app.route('/api/compare', methods=['POST'])
def compare_playthroughs():
    """Compare dialogue between two scenes or labels."""
    req_data = request.get_json(silent=True) or {}
    season1 = req_data.get('season1')
    label1 = req_data.get('label1')
    season2 = req_data.get('season2')
    label2 = req_data.get('label2')

    missing_fields = [name for name in ('season1', 'label1', 'season2', 'label2') if not req_data.get(name)]
    if missing_fields:
        return jsonify({'error': f"Missing required fields: {', '.join(missing_fields)}"}), 400
    
    data = get_game_data()
    
    scene1 = data.get('seasons', {}).get(season1, {}).get(label1)
    scene2 = data.get('seasons', {}).get(season2, {}).get(label2)

    if scene1 is None or scene2 is None:
        return jsonify({'error': 'One or both requested scenes were not found'}), 404

    scene1_dialogues = scene1.get('dialogues', [])
    scene2_dialogues = scene2.get('dialogues', [])

    counter1 = Counter(dialogue_key(dialogue) for dialogue in scene1_dialogues)
    counter2 = Counter(dialogue_key(dialogue) for dialogue in scene2_dialogues)

    lookup1 = {}
    for dialogue in scene1_dialogues:
        key = dialogue_key(dialogue)
        if key not in lookup1:
            lookup1[key] = dialogue

    lookup2 = {}
    for dialogue in scene2_dialogues:
        key = dialogue_key(dialogue)
        if key not in lookup2:
            lookup2[key] = dialogue
    
    # Find differences
    only_in_1 = [lookup1[key] for key in (counter1 - counter2).elements()]
    only_in_2 = [lookup2[key] for key in (counter2 - counter1).elements()]
    common = [lookup1[key] for key in (counter1 & counter2).elements()]
    
    return jsonify({
        'only_in_first': only_in_1,
        'only_in_second': only_in_2,
        'common': common,
        'scene1_info': {'season': season1, 'label': label1, 'total_dialogues': len(scene1_dialogues)},
        'scene2_info': {'season': season2, 'label': label2, 'total_dialogues': len(scene2_dialogues)}
    })


@app.route('/api/playthrough/compare', methods=['POST'])
def compare_full_playthroughs():
    """Compare two multi-scene playthroughs."""
    req_data = request.get_json(silent=True) or {}
    left_data = req_data.get('left_playthrough')
    right_data = req_data.get('right_playthrough')

    if not isinstance(left_data, dict) or not isinstance(right_data, dict):
        return jsonify({'error': 'Both left_playthrough and right_playthrough are required'}), 400

    if not isinstance(left_data.get('scenes', []), list) or not isinstance(right_data.get('scenes', []), list):
        return jsonify({'error': 'Each playthrough must include a scenes array'}), 400

    data = get_game_data()

    left = materialize_playthrough(left_data, data)
    right = materialize_playthrough(right_data, data)

    left_dialogues = left['dialogues']
    right_dialogues = right['dialogues']

    diff_payload = build_continuous_dialogue_diff(left_dialogues, right_dialogues)
    overview = diff_payload['overview']

    return jsonify({
        'left_info': {
            'name': left['name'],
            'input_scene_count': left['input_scene_count'],
            'resolved_scene_count': left['resolved_scene_count'],
            'total_dialogues': len(left_dialogues),
            'selected_choice_count': left.get('selected_choice_count', 0),
            'active_scene_count': left.get('active_scene_count', 0),
            'inactive_scene_count': left.get('inactive_scene_count', 0)
        },
        'right_info': {
            'name': right['name'],
            'input_scene_count': right['input_scene_count'],
            'resolved_scene_count': right['resolved_scene_count'],
            'total_dialogues': len(right_dialogues),
            'selected_choice_count': right.get('selected_choice_count', 0),
            'active_scene_count': right.get('active_scene_count', 0),
            'inactive_scene_count': right.get('inactive_scene_count', 0)
        },
        'missing_scenes': {
            'left': left['missing_scenes'],
            'right': right['missing_scenes']
        },
        'counts': {
            'common': overview['unchanged_lines'],
            'only_in_left': overview['removed_lines'],
            'only_in_right': overview['added_lines']
        },
        'samples': {
            'common': [],
            'only_in_left': [],
            'only_in_right': []
        },
        'truncated': {
            'common': False,
            'only_in_left': False,
            'only_in_right': False
        },
        'diff': diff_payload
    })


@app.route('/api/playthrough/preview', methods=['POST'])
def preview_full_playthrough():
    """Preview one playthrough and return active/inactive states for every parsed choice."""
    req_data = request.get_json(silent=True) or {}
    playthrough_data = req_data.get('playthrough')

    if not isinstance(playthrough_data, dict):
        return jsonify({'error': 'playthrough is required'}), 400

    if not isinstance(playthrough_data.get('scenes', []), list):
        return jsonify({'error': 'playthrough must include a scenes array'}), 400

    data = get_game_data()
    preview = materialize_playthrough(
        playthrough_data,
        data,
        include_dialogues=False,
        include_choice_states=True
    )

    return jsonify({
        'name': preview['name'],
        'input_scene_count': preview['input_scene_count'],
        'resolved_scene_count': preview['resolved_scene_count'],
        'selected_choice_count': preview.get('selected_choice_count', 0),
        'active_scene_count': preview.get('active_scene_count', 0),
        'inactive_scene_count': preview.get('inactive_scene_count', 0),
        'choice_state_count': len(preview.get('choice_states', {})),
        'scene_state_count': len(preview.get('scene_states', {})),
        'missing_scenes': preview['missing_scenes'],
        'resolved_scenes': preview['resolved_scenes'],
        'choice_states': preview.get('choice_states', {}),
        'scene_states': preview.get('scene_states', {})
    })


@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """Force refresh of game data (invalidate cache)."""
    global game_data
    with data_lock:
        game_data = extract_game_data(SOURCE_DIRS, use_cache=False)
    return jsonify({'status': 'refreshed', 'labels': len(game_data.get('labels', {}))})


if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    print("Starting Walkthrough Builder server...")
    print("Open http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=True)
