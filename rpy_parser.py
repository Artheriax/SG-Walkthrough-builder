"""
Ren'Py (.rpy) file parser for extracting game dialogue, choices, conditions, and scene flow.
Designed for the "Summer's Gone" visual novel series.
"""

import re
import os
import json
import hashlib
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime


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
    options: List[Dict[str, any]]  # Each option has 'text', 'line_number', 'actions'
    label: str
    line_number: int
    conditions: List[str] = field(default_factory=list)


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


@dataclass
class GameData:
    """Complete extracted data from all files."""
    seasons: Dict[str, Dict[str, SceneData]]  # season -> label -> SceneData
    labels: Dict[str, Label]  # label_name -> Label
    file_hashes: Dict[str, str]  # file_path -> hash for cache invalidation
    extraction_date: str


class RPyParser:
    """Parser for Ren'Py .rpy files."""
    
    # Pattern for dialogue lines: character_name "dialogue text"
    DIALOGUE_PATTERN = re.compile(r'^\s*(?P<speaker>[a-zA-Z_][a-zA-Z0-9_]*)\s+"(?P<text>.+)"\s*$')
    
    # Pattern for narrator text (no speaker): "text only"
    NARRATOR_PATTERN = re.compile(r'^\s*"(?P<text>.+)"\s*$')
    
    # Pattern for labels: label label_name:
    LABEL_PATTERN = re.compile(r'^label\s+(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*$')
    
    # Pattern for jumps: jump target_label
    JUMP_PATTERN = re.compile(r'^\s*jump\s+(?P<target>[a-zA-Z_][a-zA-Z0-9_]*)\s*$')
    
    # Pattern for menu/choices: menu:
    MENU_PATTERN = re.compile(r'^\s*menu\s*:\s*$')
    
    # Pattern for if statements
    IF_PATTERN = re.compile(r'^\s*(?P<type>if|elif|else)\s*(?P<condition>.*)?\s*:\s*$')
    
    # Pattern for variable assignments (to filter out)
    ASSIGNMENT_PATTERN = re.compile(r'^\s*\$?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=.*$')
    
    # Pattern for choice options in menu blocks
    CHOICE_OPTION_PATTERN = re.compile(r'^\s*"(?P<text>.+)"\s*:\s*$')
    
    def __init__(self):
        self.current_label = ""
        self.indent_stack = []
        
    def get_file_hash(self, file_path: str) -> str:
        """Calculate MD5 hash of a file for cache invalidation."""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    
    def detect_season(self, file_path: str) -> str:
        """Detect which season a file belongs to based on path."""
        if 'Season_1' in file_path or 'Season1' in file_path:
            return 'Season_1'
        elif 'Season_2' in file_path or 'Season2' in file_path:
            return 'Season_2'
        else:
            return 'Unknown'
    
    def is_game_dialogue(self, line: str, stripped: str) -> bool:
        """Check if a line contains actual game dialogue (not code)."""
        # Skip comments
        if stripped.startswith('#'):
            return False
        
        # Skip pure code lines
        if stripped.startswith('$'):
            return False
            
        # Skip define statements
        if stripped.startswith('define '):
            return False
            
        # Skip scene/show/hide statements
        if stripped.startswith(('scene ', 'show ', 'hide ', 'with ', 'pause', 
                               'stop ', 'play ', 'pass', 'return', 'call ')):
            return False
            
        # Skip empty lines
        if not stripped:
            return False
            
        return True
    
    def parse_file(self, file_path: str) -> Tuple[List[SceneData], List[Label], List[Jump]]:
        """Parse a single .rpy file and extract game data."""
        scenes = []
        labels = []
        jumps = []
        
        season = self.detect_season(file_path)
        
        current_scene_data = None
        current_dialogues = []
        current_choices = []
        current_jumps = []
        current_conditions = []
        
        in_menu = False
        menu_indent = 0
        current_menu_options = []
        menu_start_line = 0
        menu_conditions = []
        
        indent_level = 0
        condition_stack = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.rstrip('\n\r')
            content = stripped.lstrip()
            current_indent = len(stripped) - len(content)
            
            # Check for label definitions
            label_match = self.LABEL_PATTERN.match(content)
            if label_match:
                # Save previous scene if exists
                if current_scene_data and current_dialogues:
                    current_scene_data.dialogues = current_dialogues
                    current_scene_data.choices = current_choices
                    current_scene_data.jumps = current_jumps
                    current_scene_data.conditions = current_conditions
                    scenes.append(current_scene_data)
                
                label_name = label_match.group('name')
                self.current_label = label_name
                
                # Create new label entry
                label_obj = Label(
                    name=label_name,
                    line_number=line_num,
                    file_path=file_path,
                    season=season
                )
                labels.append(label_obj)
                
                # Reset for new scene
                current_dialogues = []
                current_choices = []
                current_jumps = []
                current_conditions = []
                current_scene_data = SceneData(
                    label_name=label_name,
                    dialogues=[],
                    choices=[],
                    jumps=[],
                    conditions=[]
                )
                in_menu = False
                condition_stack = []
                continue
            
            # Update current label context for jumps
            if current_scene_data is None and self.current_label:
                # We're in a label but haven't created SceneData yet
                pass
            
            # Check for jumps
            jump_match = self.JUMP_PATTERN.match(content)
            if jump_match:
                jump_obj = Jump(
                    target=jump_match.group('target'),
                    line_number=line_num,
                    source_label=self.current_label,
                    file_path=file_path
                )
                current_jumps.append(jump_obj)
                jumps.append(jump_obj)
                continue
            
            # Check for menu start
            if self.MENU_PATTERN.match(content):
                in_menu = True
                menu_indent = current_indent
                current_menu_options = []
                menu_start_line = line_num
                menu_conditions = condition_stack.copy()
                continue
            
            # Check for if/elif/else conditions
            if_match = self.IF_PATTERN.match(content)
            if if_match:
                cond_type = if_match.group('type')
                condition = if_match.group('condition') or ''
                
                if cond_type == 'else':
                    condition = 'else'
                
                cond_obj = Condition(
                    condition=condition.strip(),
                    line_number=line_num,
                    label=self.current_label,
                    block_type=cond_type
                )
                current_conditions.append(cond_obj)
                
                if cond_type == 'else':
                    condition_stack = condition_stack[:-1] if condition_stack else []
                else:
                    condition_stack.append(condition.strip())
                continue
            
            # Handle menu options
            if in_menu:
                if current_indent > menu_indent:
                    choice_match = self.CHOICE_OPTION_PATTERN.match(content)
                    if choice_match:
                        option_text = choice_match.group('text')
                        current_menu_options.append({
                            'text': option_text,
                            'line_number': line_num,
                            'conditions': condition_stack.copy()
                        })
                    continue
                else:
                    # End of menu block
                    if current_menu_options:
                        choice_obj = Choice(
                            options=current_menu_options,
                            label=self.current_label,
                            line_number=menu_start_line,
                            conditions=menu_conditions
                        )
                        current_choices.append(choice_obj)
                    in_menu = False
                    current_menu_options = []
            
            # Check for dialogue
            if not self.is_game_dialogue(line, content):
                continue
            
            # Try to match dialogue pattern
            dialogue_match = self.DIALOGUE_PATTERN.match(content)
            if dialogue_match:
                speaker = dialogue_match.group('speaker')
                text = dialogue_match.group('text')
                
                # Filter out common non-dialogue patterns
                if speaker.lower() in ('scene', 'show', 'hide', 'with', 'pause', 'stop', 'play'):
                    continue
                    
                dialogue = DialogueLine(
                    speaker=speaker,
                    text=text,
                    line_number=line_num,
                    label=self.current_label,
                    conditions=condition_stack.copy()
                )
                current_dialogues.append(dialogue)
                continue
            
            # Try narrator text
            narrator_match = self.NARRATOR_PATTERN.match(content)
            if narrator_match:
                text = narrator_match.group('text')
                dialogue = DialogueLine(
                    speaker='Narrator',
                    text=text,
                    line_number=line_num,
                    label=self.current_label,
                    conditions=condition_stack.copy()
                )
                current_dialogues.append(dialogue)
                continue
        
        # Save last scene
        if current_scene_data:
            current_scene_data.dialogues = current_dialogues
            current_scene_data.choices = current_choices
            current_scene_data.jumps = current_jumps
            current_scene_data.conditions = current_conditions
            if current_dialogues or current_choices or current_jumps:
                scenes.append(current_scene_data)
        
        return scenes, labels, jumps
    
    def parse_directory(self, directory: str) -> GameData:
        """Parse all .rpy files in a directory recursively."""
        all_scenes = {}
        all_labels = {}
        file_hashes = {}
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.rpy'):
                    file_path = os.path.join(root, file)
                    file_hash = self.get_file_hash(file_path)
                    file_hashes[file_path] = file_hash
                    
                    scenes, labels, jumps = self.parse_file(file_path)
                    
                    season = self.detect_season(file_path)
                    if season not in all_scenes:
                        all_scenes[season] = {}
                    
                    for scene in scenes:
                        key = f"{season}:{scene.label_name}"
                        all_scenes[season][scene.label_name] = scene
                    
                    for label in labels:
                        all_labels[label.name] = label
        
        return GameData(
            seasons=all_scenes,
            labels=all_labels,
            file_hashes=file_hashes,
            extraction_date=datetime.now().isoformat()
        )


class CacheManager:
    """Manages caching of extracted game data."""
    
    def __init__(self, cache_dir: str = '.cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.cache_file = os.path.join(cache_dir, 'game_data.json')
    
    def is_cache_valid(self, parser: RPyParser, source_dir: str) -> bool:
        """Check if cached data is still valid."""
        if not os.path.exists(self.cache_file):
            return False
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                cached_data = json.load(f)
            
            # Check file hashes
            cached_hashes = cached_data.get('file_hashes', {})
            for file_path, stored_hash in cached_hashes.items():
                if not os.path.exists(file_path):
                    return False
                current_hash = parser.get_file_hash(file_path)
                if current_hash != stored_hash:
                    return False
            
            return True
        except Exception:
            return False
    
    def save(self, game_data: GameData):
        """Save game data to cache."""
        # Convert dataclasses to dicts for JSON serialization
        def convert(obj):
            if hasattr(obj, '__dataclass_fields__'):
                return {k: convert(v) for k, v in asdict(obj).items()}
            elif isinstance(obj, list):
                return [convert(item) for item in obj]
            elif isinstance(obj, dict):
                return {k: convert(v) for k, v in obj.items()}
            else:
                return obj
        
        serializable = convert(game_data)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False)
    
    def load(self) -> Optional[GameData]:
        """Load game data from cache."""
        if not os.path.exists(self.cache_file):
            return None
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Convert back to dataclasses (simplified - just return dict for now)
            return data
        except Exception:
            return None


def extract_game_data(source_dirs: List[str], use_cache: bool = True) -> GameData:
    """
    Main function to extract game data from .rpy files.
    
    Args:
        source_dirs: List of directories containing .rpy files
        use_cache: Whether to use cached data if available
    
    Returns:
        GameData object containing all extracted information
    """
    parser = RPyParser()
    cache = CacheManager()
    
    # Check cache validity
    if use_cache and cache.is_cache_valid(parser, source_dirs[0]):
        print("Using cached data...")
        return cache.load()
    
    print("Extracting game data from .rpy files...")
    
    all_scenes = {}
    all_labels = {}
    file_hashes = {}
    
    for source_dir in source_dirs:
        if not os.path.exists(source_dir):
            print(f"Warning: Directory {source_dir} does not exist")
            continue
            
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith('.rpy'):
                    file_path = os.path.join(root, file)
                    print(f"  Parsing: {file_path}")
                    
                    file_hash = parser.get_file_hash(file_path)
                    file_hashes[file_path] = file_hash
                    
                    scenes, labels, jumps = parser.parse_file(file_path)
                    
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
        extraction_date=datetime.now().isoformat()
    )
    
    # Save to cache
    cache.save(game_data)
    print(f"Data cached to {cache.cache_file}")
    
    return game_data


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        source_dirs = sys.argv[1:]
    else:
        source_dirs = ['Season_1', 'Season_2']
    
    game_data = extract_game_data(source_dirs)
    
    print(f"\nExtraction complete!")
    print(f"Seasons found: {list(game_data.seasons.keys())}")
    print(f"Total labels: {len(game_data.labels)}")
    
    for season, scenes in game_data.seasons.items():
        print(f"\n{season}: {len(scenes)} scenes")
        for label_name in list(scenes.keys())[:5]:
            scene = scenes[label_name]
            print(f"  - {label_name}: {len(scene.dialogues)} dialogues, {len(scene.choices)} choices, {len(scene.jumps)} jumps")
