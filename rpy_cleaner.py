#!/usr/bin/env python3
"""
Ren'Py Cleaner - Remove presentation directives while preserving story logic.

Usage:
    python rpy_cleaner.py input_file.rpy [output_file.rpy]
    python rpy_cleaner.py --dir source_directory [--output output_directory]
"""

import os
import re
import sys
import argparse
from pathlib import Path


class RPyCleaner:
    """Clean Ren'Py .rpy files by removing scene/show/hide/pause/music etc."""

    # Patterns for lines to remove entirely (presentation-only)
    REMOVE_PATTERNS = [
        # Scene, show, hide statements
        r'^\s*scene\s+',
        r'^\s*show\s+',
        r'^\s*hide\s+',
        # Transitions and pauses
        r'^\s*with\s+',
        r'^\s*pause\b',
        r'^\s*\$?\s*renpy\.pause\s*\(',
        # Music and sound
        r'^\s*play\s+',
        r'^\s*stop\s+',
        r'^\s*queue\s+',
        r'^\s*\$?\s*play_playlist\s*\(',
        # Screen calls
        r'^\s*show\s+screen\s+',
        r'^\s*hide\s+screen\s+',
        r'^\s*call\s+screen\s+',
        # Window management
        r'^\s*window\s+(show|hide|auto)',
        # Image definitions
        r'^\s*image\s+',
        # Movie definitions
        r'^\s*\$?\s*Movie\s*\(',
    ]

    # Patterns for lines that might be mixed with logic; we keep the line
    # but these are filtered out only if they appear as standalone statements
    # (We'll handle carefully: e.g., "$ renpy.pause(1.0)" removed; "$ var = 1" kept)

    # Lines that must always be kept
    KEEP_PATTERNS = [
        r'^\s*label\s+',
        r'^\s*define\s+',
        r'^\s*default\s+',
        r'^\s*menu\s*:',
        r'^\s*jump\s+',
        r'^\s*call\s+',           # but not call screen
        r'^\s*return\b',
        r'^\s*pass\b',
        r'^\s*if\s+',
        r'^\s*elif\s+',
        r'^\s*else\s*:',
        r'^\s*while\s+',
        # Python blocks
        r'^\s*python\s*:',
        r'^\s*init\s+',
    ]

    def __init__(self):
        # Compile regexes
        self.remove_re = [re.compile(p, re.IGNORECASE) for p in self.REMOVE_PATTERNS]
        self.keep_re = [re.compile(p, re.IGNORECASE) for p in self.KEEP_PATTERNS]

        # Dialogue pattern: speaker "text"
        self.dialogue_re = re.compile(r'^\s*(?P<speaker>[a-zA-Z_][a-zA-Z0-9_]*)\s+"(?P<text>.*)"\s*$')
        # Narrator dialogue: "text"
        self.narrator_re = re.compile(r'^\s*"(?P<text>.*)"\s*$')

        # Python assignment: $ var = expr or $ var += expr
        self.assign_re = re.compile(r'^\s*\$?\s*(?P<target>[a-zA-Z_][a-zA-Z0-9_\.]*)\s*(?P<op>=|\+=|-=|\*=|\/=)\s*(?P<expr>.+?)\s*$')
        # Method call: $ obj.method(args)
        self.method_call_re = re.compile(r'^\s*\$?\s*(?P<target>[a-zA-Z_][a-zA-Z0-9_\.]*)\s*\.(?P<method>[a-zA-Z_][a-zA-Z0-9_]*)\s*\((?P<args>.*)\)\s*$')
        # Achievement: $ achievement.grant(...)
        self.achievement_re = re.compile(r'^\s*\$?\s*achievement\.\w+\s*\(')

        # Comments
        self.comment_re = re.compile(r'^\s*#')

    def should_remove_line(self, line: str) -> bool:
        """Return True if the line is purely presentation and can be removed."""
        stripped = line.strip()
        if not stripped:
            return False  # keep empty lines for structure

        # Keep comments (they may contain useful info)
        if self.comment_re.match(line):
            return False

        # Keep lines that are essential structure
        for pattern in self.keep_re:
            if pattern.match(line):
                return False

        # Keep dialogue
        if self.dialogue_re.match(line) or self.narrator_re.match(line):
            return False

        # Keep assignments and method calls (state changes)
        if self.assign_re.match(line):
            return False
        if self.method_call_re.match(line):
            return False
        if self.achievement_re.search(line):
            return False

        # Check removal patterns
        for pattern in self.remove_re:
            if pattern.match(line):
                return True

        # Special case: $ renpy.input (we want to keep it)
        if 'renpy.input' in line:
            return False

        # By default, keep unknown lines (might be dialogue continuation or other logic)
        return False

    def clean_line(self, line: str) -> str:
        """Process a single line, returning it if kept, or None if removed."""
        if self.should_remove_line(line):
            return None
        return line

    def clean_content(self, content: str) -> str:
        """Clean an entire .rpy file content."""
        lines = content.splitlines(keepends=True)
        cleaned_lines = []

        # We need to track indentation to handle block structures correctly.
        # Simple approach: keep lines as-is unless removed; preserve empty lines.
        in_multiline_string = False
        multiline_delimiter = None

        for line in lines:
            # Skip multiline string handling for simplicity; assume no crucial logic inside.
            # (In practice, dialogue is single-line, and python blocks we keep.)
            cleaned = self.clean_line(line.rstrip('\n\r'))
            if cleaned is not None:
                cleaned_lines.append(cleaned + '\n')

        return ''.join(cleaned_lines)

    def clean_file(self, input_path: Path, output_path: Path):
        """Clean a single .rpy file."""
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = self.clean_content(content)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"Cleaned: {input_path} -> {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Clean Ren'Py .rpy files of presentation directives.")
    parser.add_argument('input', help='Input .rpy file or directory (with --dir)')
    parser.add_argument('output', nargs='?', help='Output file (if input is a single file)')
    parser.add_argument('--dir', action='store_true', help='Process a directory recursively')
    parser.add_argument('--output-dir', help='Output directory (when using --dir)')
    args = parser.parse_args()

    cleaner = RPyCleaner()

    if args.dir:
        input_dir = Path(args.input)
        if not input_dir.is_dir():
            print(f"Error: {args.input} is not a directory.")
            sys.exit(1)

        output_dir = Path(args.output_dir) if args.output_dir else input_dir.parent / (input_dir.name + '_cleaned')
        output_dir.mkdir(parents=True, exist_ok=True)

        for rpy_file in input_dir.rglob('*.rpy'):
            rel_path = rpy_file.relative_to(input_dir)
            out_file = output_dir / rel_path
            cleaner.clean_file(rpy_file, out_file)
        print(f"All .rpy files processed. Output directory: {output_dir}")
    else:
        input_path = Path(args.input)
        if not input_path.is_file():
            print(f"Error: {args.input} is not a file.")
            sys.exit(1)

        if args.output:
            output_path = Path(args.output)
        else:
            output_path = input_path.with_name(input_path.stem + '_clean' + input_path.suffix)

        cleaner.clean_file(input_path, output_path)


if __name__ == '__main__':
    main()