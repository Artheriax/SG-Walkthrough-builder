"""
Ren'Py (.rpy) file parser for extracting game dialogue, choices, conditions, and scene flow.
Enhanced version with support for call statements, method calls, persistent variables, and renpy.input.
"""

import re
import os
import json
import ast
import hashlib
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple, Any, Union
from datetime import datetime


PARSER_VERSION = "2026-04-enhanced-call-and-actions-v2"


@dataclass
class DialogueLine:
    """Represents a single line of dialogue."""

    speaker: str
    text: str
    line_number: int
    label: str  # Current label/scene context
    conditions: List[str] = field(default_factory=list)  # Conditions that must be met


@dataclass
class Choice:
    """Represents a menu choice."""

    options: List[Dict[str, Any]]  # Each option has 'text', 'line_number', 'actions'
    label: str
    line_number: int
    conditions: List[str] = field(default_factory=list)
    nesting_level: int = 0
    parent_choice_line: Optional[int] = None
    parent_option_index: Optional[int] = None
    parent_option_text: str = ""


@dataclass
class Label:
    """Represents a label (scene entry point)."""

    name: str
    line_number: int
    file_path: str
    season: str


@dataclass
class Jump:
    """Represents a jump statement."""

    target: str
    line_number: int
    source_label: str
    file_path: str
    conditions: List[str] = field(default_factory=list)


@dataclass
class Call:
    """Represents a call statement."""

    target: str
    line_number: int
    source_label: str
    file_path: str
    conditions: List[str] = field(default_factory=list)


@dataclass
class CallScreen:
    """Represents a call screen statement."""

    screen_name: str
    line_number: int
    source_label: str
    file_path: str
    conditions: List[str] = field(default_factory=list)


@dataclass
class Condition:
    """Represents a conditional block."""

    condition: str
    line_number: int
    label: str
    block_type: str  # 'if', 'elif', 'else'


@dataclass
class SceneData:
    """Complete extracted data from a scene/label."""

    label_name: str
    dialogues: List[DialogueLine]
    choices: List[Choice]
    jumps: List[Jump]
    conditions: List[Condition]
    calls: List[Call] = field(default_factory=list)
    call_screens: List[CallScreen] = field(default_factory=list)
    state_actions: List[Dict[str, Any]] = field(default_factory=list)
    file_path: str = ""
    label_line_number: Optional[int] = None


@dataclass
class GameData:
    """Complete extracted data from all files."""

    seasons: Dict[str, Dict[str, SceneData]]  # season -> label -> SceneData
    labels: Dict[str, Label]  # label_name -> Label
    file_hashes: Dict[str, str]  # file_path -> hash for cache invalidation
    extraction_date: str
    parser_version: str


class RPyParser:
    """Parser for Ren'Py .rpy files."""

    # Pattern for dialogue lines: character_name "dialogue text"
    DIALOGUE_PATTERN = re.compile(
        r'^\s*(?P<speaker>[a-zA-Z_][a-zA-Z0-9_]*)\s+"(?P<text>.+)"\s*$'
    )

    # Pattern for narrator text (no speaker): "text only"
    NARRATOR_PATTERN = re.compile(r'^\s*"(?P<text>.+)"\s*$')

    # Pattern for labels: label label_name:
    LABEL_PATTERN = re.compile(
        r"^label\s+(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(?:#.*)?$"
    )

    # Pattern for jumps: jump target_label
    JUMP_PATTERN = re.compile(r"^\s*jump\s+(?P<target>[a-zA-Z_][a-zA-Z0-9_]*)\s*$")

    # Pattern for calls: call target_label
    CALL_PATTERN = re.compile(r"^\s*call\s+(?P<target>[a-zA-Z_][a-zA-Z0-9_]*)\s*$")

    # Pattern for call screen: call screen screen_name
    CALL_SCREEN_PATTERN = re.compile(
        r"^\s*call\s+screen\s+(?P<screen>[a-zA-Z_][a-zA-Z0-9_]*)\s*$"
    )

    # Pattern for return statement
    RETURN_PATTERN = re.compile(r"^\s*return\s*$")

    # Pattern for menu/choices: menu:
    MENU_PATTERN = re.compile(r"^\s*menu\s*:\s*$")

    # Pattern for if statements
    IF_PATTERN = re.compile(r"^\s*(?P<type>if|elif|else)\s*(?P<condition>.*)?\s*:\s*$")

    # Pattern for variable assignments (to filter out)
    ASSIGNMENT_PATTERN = re.compile(r"^\s*\$?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=.*$")

    # Pattern for choice options in menu blocks
    CHOICE_OPTION_PATTERN = re.compile(
        r'^\s*"(?P<text>.+?)"\s*(?:if\s+(?P<if_condition>.+?))?\s*:\s*$'
    )

    # Pattern for character aliases: define x = Character('Display Name', ...)
    DEFINE_CHARACTER_PATTERN = re.compile(
        r'^\s*define\s+(?P<alias>[a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*Character\(\s*(?P<name>"[^"]*"|\'[^\']*\')',
        re.IGNORECASE,
    )

    # Pattern for variable assignments inside choice branches (simple)
    CHOICE_ASSIGNMENT_PATTERN = re.compile(
        r"^\s*\$?\s*(?P<target>[a-zA-Z_][a-zA-Z0-9_\.]*)\s*(?P<op>\+=|-=|\*=|/=|=)\s*(?P<expr>.+?)\s*$"
    )

    # Pattern for renpy.input calls
    RENPY_INPUT_PATTERN = re.compile(
        r"^\s*\$?\s*(?P<target>[a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*renpy\.input\s*\((?P<args>.*)\)\s*$"
    )

    # Pattern for persistent variable assignments
    PERSISTENT_ASSIGN_PATTERN = re.compile(
        r"^\s*\$?\s*persistent\.(?P<attr>[a-zA-Z_][a-zA-Z0-9_]*)\s*(?P<op>=|\+=|-=)\s*(?P<expr>.+?)\s*$"
    )

    # Pattern for default persistent
    DEFAULT_PERSISTENT_PATTERN = re.compile(
        r"^\s*default\s+persistent\.(?P<attr>[a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?P<expr>.+?)\s*$"
    )

    # Pattern for method calls (e.g., list.append, achievement.grant)
    METHOD_CALL_PATTERN = re.compile(
        r"^\s*\$?\s*(?P<target>[a-zA-Z_][a-zA-Z0-9_\.]*)\s*\.(?P<method>[a-zA-Z_][a-zA-Z0-9_]*)\s*\((?P<args>.*)\)\s*$"
    )

    def __init__(self):
        self.current_label = ""
        self.indent_stack = []

    def parse_character_definition(self, content: str) -> Optional[Tuple[str, str]]:
        """Extract one alias->display-name pair from a define Character line."""
        match = self.DEFINE_CHARACTER_PATTERN.match(content or "")
        if not match:
            return None

        alias = str(match.group("alias") or "").strip()
        name_token = str(match.group("name") or "").strip()
        if not alias or not name_token:
            return None

        try:
            display_name = ast.literal_eval(name_token)
        except Exception:
            display_name = name_token[1:-1]

        display_name = str(display_name or "").strip()
        if not display_name:
            return None

        return alias, display_name

    def collect_character_aliases(self, file_paths: List[str]) -> Dict[str, str]:
        """Collect global character aliases so files without local defines still resolve names."""
        aliases: Dict[str, str] = {}

        for file_path in sorted(file_paths):
            try:
                with open(file_path, "r", encoding="utf-8") as handle:
                    for raw_line in handle:
                        content = raw_line.rstrip("\n\r").lstrip()
                        parsed = self.parse_character_definition(content)
                        if parsed:
                            alias, display_name = parsed
                            aliases[alias] = display_name
            except Exception:
                continue

        return aliases

    def get_file_hash(self, file_path: str) -> str:
        """Calculate MD5 hash of a file for cache invalidation."""
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def detect_season(self, file_path: str) -> str:
        """Detect which season a file belongs to based on path."""
        if "Season_1" in file_path or "Season1" in file_path:
            return "Season_1"
        elif "Season_2" in file_path or "Season2" in file_path:
            return "Season_2"
        else:
            return "Unknown"

    def is_game_dialogue(self, line: str, stripped: str) -> bool:
        """Check if a line contains actual game dialogue (not code)."""
        # Skip comments
        if stripped.startswith("#"):
            return False

        # Skip pure code lines
        if stripped.startswith("$"):
            return False

        # Skip define statements
        if stripped.startswith("define "):
            return False

        # Skip scene/show/hide statements
        if stripped.startswith(
            (
                "scene ",
                "show ",
                "hide ",
                "with ",
                "pause",
                "stop ",
                "play ",
                "pass",
                "return",
                "call ",
            )
        ):
            return False

        # Skip empty lines
        if not stripped:
            return False

        return True

    def parse_file(
        self, file_path: str, base_character_aliases: Optional[Dict[str, str]] = None
    ) -> Tuple[List[SceneData], List[Label], List[Jump]]:
        """Parse a single .rpy file and extract game data."""
        scenes = []
        labels = []
        jumps = []
        character_aliases = dict(base_character_aliases or {})

        season = self.detect_season(file_path)

        current_scene_data = None
        current_dialogues = []
        current_choices = []
        current_jumps = []
        current_calls = []
        current_call_screens = []
        current_conditions = []
        current_state_actions = []

        menu_stack: List[Dict[str, Any]] = []

        condition_stack: List[Tuple[int, str]] = []
        condition_branch_history: Dict[int, List[str]] = {}

        def active_conditions() -> List[str]:
            return [condition for _, condition in condition_stack]

        def negate_branch_history(branch_conditions: List[str]) -> str:
            normalized = [
                str(condition or "").strip() for condition in branch_conditions
            ]
            normalized = [condition for condition in normalized if condition]
            if not normalized:
                return ""

            joined = " or ".join(f"({condition})" for condition in normalized)
            return f"not ({joined})"

        def flush_menu_choice(menu_ctx: Optional[Dict[str, Any]]):
            if not menu_ctx:
                return

            options = menu_ctx.get("options", [])
            if not options:
                return

            choice_obj = Choice(
                options=options,
                label=self.current_label,
                line_number=menu_ctx.get("start_line", 0),
                conditions=menu_ctx.get("conditions", []),
                nesting_level=menu_ctx.get("nesting_level", 0),
                parent_choice_line=menu_ctx.get("parent_choice_line"),
                parent_option_index=menu_ctx.get("parent_option_index"),
                parent_option_text=menu_ctx.get("parent_option_text", ""),
            )
            current_choices.append(choice_obj)

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            stripped = line.rstrip("\n\r")
            content = stripped.lstrip()
            current_indent = len(stripped) - len(content)

            # Check for label definitions
            label_match = self.LABEL_PATTERN.match(content)
            if label_match:
                while menu_stack:
                    flush_menu_choice(menu_stack.pop())

                # Save previous scene if exists
                if current_scene_data and (
                    current_dialogues
                    or current_choices
                    or current_jumps
                    or current_calls
                    or current_call_screens
                    or current_state_actions
                ):
                    current_scene_data.dialogues = current_dialogues
                    current_scene_data.choices = sorted(
                        current_choices,
                        key=lambda choice: (
                            (
                                choice.line_number
                                if isinstance(choice.line_number, int)
                                else 10**9
                            ),
                            choice.nesting_level,
                        ),
                    )
                    current_scene_data.jumps = current_jumps
                    current_scene_data.calls = current_calls
                    current_scene_data.call_screens = current_call_screens
                    current_scene_data.conditions = current_conditions
                    current_scene_data.state_actions = current_state_actions
                    scenes.append(current_scene_data)

                label_name = label_match.group("name")
                self.current_label = label_name

                # Create new label entry
                label_obj = Label(
                    name=label_name,
                    line_number=line_num,
                    file_path=file_path,
                    season=season,
                )
                labels.append(label_obj)

                # Reset for new scene
                current_dialogues = []
                current_choices = []
                current_jumps = []
                current_calls = []
                current_call_screens = []
                current_conditions = []
                current_state_actions = []
                current_scene_data = SceneData(
                    label_name=label_name,
                    dialogues=[],
                    choices=[],
                    jumps=[],
                    calls=[],
                    call_screens=[],
                    conditions=[],
                    state_actions=[],
                    file_path=file_path,
                    label_line_number=line_num,
                )
                menu_stack = []
                condition_stack = []
                continue

            # Keep condition context in sync with block indentation.
            if content and not content.startswith("#"):
                while condition_stack and current_indent <= condition_stack[-1][0]:
                    condition_stack.pop()

                for indent_level in list(condition_branch_history.keys()):
                    if indent_level > current_indent:
                        condition_branch_history.pop(indent_level, None)

                if (
                    current_indent in condition_branch_history
                    and not self.IF_PATTERN.match(content)
                ):
                    condition_branch_history.pop(current_indent, None)

                while menu_stack and current_indent <= menu_stack[-1]["indent"]:
                    flush_menu_choice(menu_stack.pop())

            # Update current label context for jumps
            if current_scene_data is None and self.current_label:
                # We're in a label but haven't created SceneData yet
                pass

            # Capture alias->name definitions so dialogue speakers can use full names.
            character_definition = self.parse_character_definition(content)
            if character_definition:
                alias, display_name = character_definition
                character_aliases[alias] = display_name
                continue

            # Check for jumps
            jump_match = self.JUMP_PATTERN.match(content)
            if jump_match:
                jump_conditions = active_conditions()

                # If this jump is inside a menu option branch, bind it to that
                # specific choice option so downstream activation can respect the
                # user's selected option instead of treating all option jumps as unconditional.
                if menu_stack:
                    active_menu = menu_stack[-1]
                    current_option = active_menu.get("current_option")
                    current_option_indent = active_menu.get("current_option_indent", 0)
                    if current_option and current_indent > current_option_indent:
                        option_index = current_option.get("option_index")
                        menu_start_line = active_menu.get("start_line")
                        if isinstance(menu_start_line, int) and isinstance(
                            option_index, int
                        ):
                            jump_conditions = [
                                *jump_conditions,
                                f"__choice_{menu_start_line} == {option_index}",
                            ]

                        current_option_actions = current_option.get("actions", [])
                        current_option_actions.append(
                            {
                                "type": "jump",
                                "target": jump_match.group("target").strip(),
                                "line_number": line_num,
                            }
                        )
                        current_option["actions"] = current_option_actions

                jump_obj = Jump(
                    target=jump_match.group("target"),
                    line_number=line_num,
                    source_label=self.current_label,
                    file_path=file_path,
                    conditions=jump_conditions,
                )
                current_jumps.append(jump_obj)
                jumps.append(jump_obj)
                continue

            # Check for call statements
            call_match = self.CALL_PATTERN.match(content)
            if call_match:
                call_conditions = active_conditions()
                # Similar menu option binding as for jumps
                if menu_stack:
                    active_menu = menu_stack[-1]
                    current_option = active_menu.get("current_option")
                    current_option_indent = active_menu.get("current_option_indent", 0)
                    if current_option and current_indent > current_option_indent:
                        option_index = current_option.get("option_index")
                        menu_start_line = active_menu.get("start_line")
                        if isinstance(menu_start_line, int) and isinstance(
                            option_index, int
                        ):
                            call_conditions = [
                                *call_conditions,
                                f"__choice_{menu_start_line} == {option_index}",
                            ]
                        current_option_actions = current_option.get("actions", [])
                        current_option_actions.append(
                            {
                                "type": "call",
                                "target": call_match.group("target").strip(),
                                "line_number": line_num,
                            }
                        )
                        current_option["actions"] = current_option_actions

                call_obj = Call(
                    target=call_match.group("target"),
                    line_number=line_num,
                    source_label=self.current_label,
                    file_path=file_path,
                    conditions=call_conditions,
                )
                current_calls.append(call_obj)
                continue

            # Check for call screen statements
            call_screen_match = self.CALL_SCREEN_PATTERN.match(content)
            if call_screen_match:
                call_screen_conditions = active_conditions()
                # Menu option binding
                if menu_stack:
                    active_menu = menu_stack[-1]
                    current_option = active_menu.get("current_option")
                    current_option_indent = active_menu.get("current_option_indent", 0)
                    if current_option and current_indent > current_option_indent:
                        current_option_actions = current_option.get("actions", [])
                        current_option_actions.append(
                            {
                                "type": "call_screen",
                                "screen": call_screen_match.group("screen").strip(),
                                "line_number": line_num,
                            }
                        )
                        current_option["actions"] = current_option_actions

                call_screen_obj = CallScreen(
                    screen_name=call_screen_match.group("screen"),
                    line_number=line_num,
                    source_label=self.current_label,
                    file_path=file_path,
                    conditions=call_screen_conditions,
                )
                current_call_screens.append(call_screen_obj)
                continue

            # Check for return statement
            return_match = self.RETURN_PATTERN.match(content)
            if return_match:
                return_conditions = active_conditions()
                current_state_actions.append(
                    {
                        "type": "return",
                        "line_number": line_num,
                        "conditions": return_conditions,
                    }
                )
                continue

            # Check for menu start
            if self.MENU_PATTERN.match(content):
                parent_choice_line = None
                parent_option_index = None
                parent_option_text = ""
                nesting_level = len(menu_stack)

                if menu_stack:
                    parent_ctx = menu_stack[-1]
                    parent_option = parent_ctx.get("current_option")
                    parent_option_indent = parent_ctx.get("current_option_indent", -1)
                    if parent_option and current_indent > parent_option_indent:
                        parent_choice_line = parent_ctx.get("start_line")
                        parent_option_index = parent_option.get("option_index")
                        parent_option_text = parent_option.get("text", "")

                menu_stack.append(
                    {
                        "indent": current_indent,
                        "start_line": line_num,
                        "conditions": active_conditions(),
                        "options": [],
                        "current_option": None,
                        "current_option_indent": 0,
                        "nesting_level": nesting_level,
                        "parent_choice_line": parent_choice_line,
                        "parent_option_index": parent_option_index,
                        "parent_option_text": parent_option_text,
                    }
                )
                continue

            # Check for if/elif/else conditions
            if_match = self.IF_PATTERN.match(content)
            if if_match:
                cond_type = if_match.group("type")
                raw_condition = (if_match.group("condition") or "").strip()

                if cond_type == "if":
                    effective_condition = raw_condition
                    condition_branch_history[current_indent] = (
                        [raw_condition] if raw_condition else []
                    )
                    display_condition = raw_condition
                elif cond_type == "elif":
                    previous_conditions = condition_branch_history.get(
                        current_indent, []
                    )
                    guard_condition = negate_branch_history(previous_conditions)

                    if guard_condition and raw_condition:
                        effective_condition = (
                            f"({guard_condition}) and ({raw_condition})"
                        )
                    else:
                        effective_condition = raw_condition or guard_condition

                    updated_conditions = [*previous_conditions]
                    if raw_condition:
                        updated_conditions.append(raw_condition)
                    condition_branch_history[current_indent] = updated_conditions
                    display_condition = raw_condition
                else:
                    previous_conditions = condition_branch_history.get(
                        current_indent, []
                    )
                    guard_condition = negate_branch_history(previous_conditions)
                    effective_condition = guard_condition or "else"
                    display_condition = "else"

                cond_obj = Condition(
                    condition=display_condition,
                    line_number=line_num,
                    label=self.current_label,
                    block_type=cond_type,
                )
                current_conditions.append(cond_obj)

                condition_stack.append(
                    (current_indent, str(effective_condition).strip() or "else")
                )
                continue

            # Handle menu options
            if menu_stack:
                active_menu = menu_stack[-1]
                if current_indent > active_menu["indent"]:
                    choice_match = self.CHOICE_OPTION_PATTERN.match(content)
                    if choice_match:
                        option_text = choice_match.group("text")
                        inline_condition = (
                            choice_match.group("if_condition") or ""
                        ).strip()
                        option_conditions = active_conditions()
                        if inline_condition:
                            option_conditions = [*option_conditions, inline_condition]

                        option_index = len(active_menu["options"])
                        option_data = {
                            "text": option_text,
                            "line_number": line_num,
                            "conditions": option_conditions,
                            "actions": [],
                            "option_index": option_index,
                        }
                        active_menu["options"].append(option_data)
                        active_menu["current_option"] = option_data
                        active_menu["current_option_indent"] = current_indent
                        continue

                    current_option = active_menu.get("current_option")
                    current_option_indent = active_menu.get("current_option_indent", 0)
                    if current_option and current_indent > current_option_indent:
                        assignment_match = self.CHOICE_ASSIGNMENT_PATTERN.match(content)
                        if assignment_match:
                            current_option_actions = current_option.get("actions", [])
                            current_option_actions.append(
                                {
                                    "type": "assign",
                                    "target": assignment_match.group("target").strip(),
                                    "op": assignment_match.group("op").strip(),
                                    "expression": assignment_match.group(
                                        "expr"
                                    ).strip(),
                                    "line_number": line_num,
                                }
                            )
                            current_option["actions"] = current_option_actions
                            continue

                        option_jump_match = self.JUMP_PATTERN.match(content)
                        if option_jump_match:
                            current_option_actions = current_option.get("actions", [])
                            current_option_actions.append(
                                {
                                    "type": "jump",
                                    "target": option_jump_match.group("target").strip(),
                                    "line_number": line_num,
                                }
                            )
                            current_option["actions"] = current_option_actions

                        # Also capture calls inside options
                        option_call_match = self.CALL_PATTERN.match(content)
                        if option_call_match:
                            current_option_actions = current_option.get("actions", [])
                            current_option_actions.append(
                                {
                                    "type": "call",
                                    "target": option_call_match.group("target").strip(),
                                    "line_number": line_num,
                                }
                            )
                            current_option["actions"] = current_option_actions
                    continue

            # Track non-choice state assignments so scene activation conditions can
            # evaluate variables that are set in regular script flow.
            assignment_match = self.CHOICE_ASSIGNMENT_PATTERN.match(content)
            if assignment_match and current_scene_data is not None:
                current_state_actions.append(
                    {
                        "type": "assign",
                        "target": assignment_match.group("target").strip(),
                        "op": assignment_match.group("op").strip(),
                        "expression": assignment_match.group("expr").strip(),
                        "line_number": line_num,
                        "conditions": active_conditions(),
                    }
                )
                continue

            # Check for renpy.input
            input_match = self.RENPY_INPUT_PATTERN.match(content)
            if input_match:
                target = input_match.group("target")
                args = input_match.group("args").strip()
                # Parse default value from args
                default_match = re.search(r'default\s*=\s*"([^"]*)"', args)
                default_value = default_match.group(1) if default_match else ""
                current_state_actions.append(
                    {
                        "type": "input",
                        "target": target,
                        "default": default_value,
                        "line_number": line_num,
                        "conditions": active_conditions(),
                    }
                )
                continue

            # Check for persistent assignments
            persist_match = self.PERSISTENT_ASSIGN_PATTERN.match(content)
            if persist_match:
                attr = persist_match.group("attr")
                op = persist_match.group("op")
                expr = persist_match.group("expr").strip()
                current_state_actions.append(
                    {
                        "type": "persistent_assign",
                        "target": f"persistent.{attr}",
                        "op": op,
                        "expression": expr,
                        "line_number": line_num,
                        "conditions": active_conditions(),
                    }
                )
                continue

            # Check for default persistent
            default_persist_match = self.DEFAULT_PERSISTENT_PATTERN.match(content)
            if default_persist_match:
                attr = default_persist_match.group("attr")
                expr = default_persist_match.group("expr").strip()
                current_state_actions.append(
                    {
                        "type": "persistent_default",
                        "target": f"persistent.{attr}",
                        "expression": expr,
                        "line_number": line_num,
                        "conditions": active_conditions(),
                    }
                )
                continue

            # Check for method calls (after assignments to avoid false positives)
            method_match = self.METHOD_CALL_PATTERN.match(content)
            if method_match:
                target = method_match.group("target")
                method = method_match.group("method")
                args = method_match.group("args").strip()
                current_state_actions.append(
                    {
                        "type": "method_call",
                        "target": target,
                        "method": method,
                        "args": args,
                        "line_number": line_num,
                        "conditions": active_conditions(),
                    }
                )
                continue

            # Check for dialogue
            if not self.is_game_dialogue(line, content):
                continue

            # Try to match dialogue pattern
            dialogue_match = self.DIALOGUE_PATTERN.match(content)
            if dialogue_match:
                speaker = dialogue_match.group("speaker")
                text = dialogue_match.group("text")

                # Filter out common non-dialogue patterns
                if speaker.lower() in (
                    "scene",
                    "show",
                    "hide",
                    "with",
                    "pause",
                    "stop",
                    "play",
                ):
                    continue

                dialogue = DialogueLine(
                    speaker=character_aliases.get(speaker, speaker),
                    text=text,
                    line_number=line_num,
                    label=self.current_label,
                    conditions=active_conditions(),
                )
                current_dialogues.append(dialogue)
                continue

            # Try narrator text
            narrator_match = self.NARRATOR_PATTERN.match(content)
            if narrator_match:
                text = narrator_match.group("text")
                dialogue = DialogueLine(
                    speaker="Narrator",
                    text=text,
                    line_number=line_num,
                    label=self.current_label,
                    conditions=active_conditions(),
                )
                current_dialogues.append(dialogue)
                continue

        while menu_stack:
            flush_menu_choice(menu_stack.pop())

        # Save last scene
        if current_scene_data:
            current_scene_data.dialogues = current_dialogues
            current_scene_data.choices = sorted(
                current_choices,
                key=lambda choice: (
                    (
                        choice.line_number
                        if isinstance(choice.line_number, int)
                        else 10**9
                    ),
                    choice.nesting_level,
                ),
            )
            current_scene_data.jumps = current_jumps
            current_scene_data.calls = current_calls
            current_scene_data.call_screens = current_call_screens
            current_scene_data.conditions = current_conditions
            current_scene_data.state_actions = current_state_actions
            if (
                current_dialogues
                or current_choices
                or current_jumps
                or current_calls
                or current_state_actions
            ):
                scenes.append(current_scene_data)

        return scenes, labels, jumps

    def parse_directory(self, directory: str) -> GameData:
        """Parse all .rpy files in a directory recursively."""
        all_scenes = {}
        all_labels = {}
        file_hashes = {}

        file_paths = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".rpy"):
                    file_paths.append(os.path.join(root, file))

        file_paths.sort()

        for file_path in file_paths:
            file_hashes[file_path] = self.get_file_hash(file_path)

        base_character_aliases = self.collect_character_aliases(file_paths)

        for file_path in file_paths:
            scenes, labels, jumps = self.parse_file(
                file_path, base_character_aliases=base_character_aliases
            )

            season = self.detect_season(file_path)
            if season not in all_scenes:
                all_scenes[season] = {}

            for scene in scenes:
                all_scenes[season][scene.label_name] = scene

            for label in labels:
                all_labels[label.name] = label

        return GameData(
            seasons=all_scenes,
            labels=all_labels,
            file_hashes=file_hashes,
            extraction_date=datetime.now().isoformat(),
            parser_version=PARSER_VERSION,
        )


class CacheManager:
    """Manages caching of extracted game data."""

    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.cache_file = os.path.join(cache_dir, "game_data.json")

    def is_cache_valid(
        self, parser: RPyParser, source_dirs: Union[str, List[str]]
    ) -> bool:
        """Check if cached data is still valid."""
        if not os.path.exists(self.cache_file):
            return False

        if isinstance(source_dirs, str):
            source_dirs = [source_dirs]

        try:
            with open(self.cache_file, "r", encoding="utf-8") as f:
                cached_data = json.load(f)

            # Build current hash map from the actual source directories.
            current_hashes = {}
            for source_dir in source_dirs:
                if not os.path.exists(source_dir):
                    continue

                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        if file.endswith(".rpy"):
                            file_path = os.path.join(root, file)
                            current_hashes[file_path] = parser.get_file_hash(file_path)

            if not current_hashes:
                return False

            # Check file hashes
            cached_hashes = cached_data.get("file_hashes", {})

            # If files were added/removed, cache is stale.
            if set(cached_hashes.keys()) != set(current_hashes.keys()):
                return False

            for file_path, current_hash in current_hashes.items():
                if cached_hashes.get(file_path) != current_hash:
                    return False

            return True
        except Exception:
            return False

    def save(self, game_data: GameData):
        """Save game data to cache."""

        # Convert dataclasses to dicts for JSON serialization
        def convert(obj):
            if hasattr(obj, "__dataclass_fields__"):
                return {k: convert(v) for k, v in asdict(obj).items()}
            elif isinstance(obj, list):
                return [convert(item) for item in obj]
            elif isinstance(obj, dict):
                return {k: convert(v) for k, v in obj.items()}
            else:
                return obj

        serializable = convert(game_data)

        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False)

    def load(self) -> Optional[Dict[str, Any]]:
        """Load game data from cache."""
        if not os.path.exists(self.cache_file):
            return None

        try:
            with open(self.cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return data
        except Exception:
            return None


def extract_game_data(source_dirs: List[str], use_cache: bool = True) -> Dict[str, Any]:
    """
    Main function to extract game data from .rpy files.

    Args:
        source_dirs: List of directories containing .rpy files
        use_cache: Whether to use cached data if available

    Returns:
        Dict containing all extracted information
    """
    parser = RPyParser()
    cache = CacheManager()

    # Check cache validity
    if use_cache and cache.is_cache_valid(parser, source_dirs):
        cached_data = cache.load()
        if cached_data is not None:
            print("Using cached data...")
            return cached_data

    print("Extracting game data from .rpy files...")

    all_scenes = {}
    all_labels = {}
    file_hashes = {}

    all_file_paths = []
    for source_dir in source_dirs:
        if not os.path.exists(source_dir):
            print(f"Warning: Directory {source_dir} does not exist")
            continue

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith(".rpy"):
                    all_file_paths.append(os.path.join(root, file))

    all_file_paths.sort()

    for file_path in all_file_paths:
        file_hashes[file_path] = parser.get_file_hash(file_path)

    base_character_aliases = parser.collect_character_aliases(all_file_paths)

    for file_path in all_file_paths:
        print(f"  Parsing: {file_path}")

        scenes, labels, jumps = parser.parse_file(
            file_path, base_character_aliases=base_character_aliases
        )

        season = parser.detect_season(file_path)
        if season not in all_scenes:
            all_scenes[season] = {}

        for scene in scenes:
            all_scenes[season][scene.label_name] = scene

        for label in labels:
            all_labels[label.name] = label

    game_data = GameData(
        seasons=all_scenes,
        labels=all_labels,
        file_hashes=file_hashes,
        extraction_date=datetime.now().isoformat(),
        parser_version=PARSER_VERSION,
    )

    # Save to cache
    cache.save(game_data)
    print(f"Data cached to {cache.cache_file}")

    return asdict(game_data)


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) > 1:
        source_dirs = sys.argv[1:]
    else:
        source_dirs = ["Season_1", "Season_2"]

    game_data = extract_game_data(source_dirs)

    print(f"\nExtraction complete!")
    print(f"Seasons found: {list(game_data['seasons'].keys())}")
    print(f"Total labels: {len(game_data['labels'])}")

    for season, scenes in game_data["seasons"].items():
        print(f"\n{season}: {len(scenes)} scenes")
        for label_name in list(scenes.keys())[:5]:
            scene = scenes[label_name]
            print(
                f"  - {label_name}: {len(scene.get('dialogues', []))} dialogues, "
                f"{len(scene.get('choices', []))} choices, {len(scene.get('jumps', []))} jumps"
            )
