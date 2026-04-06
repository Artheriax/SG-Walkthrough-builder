# Summer's Gone Walkthrough Builder

A modern, modular tool for extracting and comparing dialogue from Ren'Py visual novel files (.rpy). Built specifically for "Summer's Gone" Season 1 & 2.

## Features

- **Scene-Aware Extraction**: Properly tracks labels and jumps to maintain scene context
- **Dialogue Extraction**: Extracts all character dialogue and narrator text
- **Choice Tracking**: Captures all menu choices with their conditions
- **Condition Tracking**: Tracks if/elif/else conditions that affect dialogue
- **Jump Detection**: Identifies scene transitions via jump statements
- **Smart Caching**: Uses JSON cache with file hash validation for fast reloads
- **Playthrough Lab UI**: Auto-loads the full story on both sides for side-by-side comparison
- **Full Run Panels**: Before comparing, each side shows one long season/chapter/scene list with scenes, choices, and conditions
- **Stream-Only UI**: Timeline and scene preview panels are removed; full-story streams are always visible
- **Choice Option Selection**: Pick different options per side to simulate variable changes and branch differences
- **Continuous Diff Overview**: Compare full playthroughs as a seamless GitHub-style line diff

## Project Structure

```text
SG Walkthrough builder/
├── rpy_parser.py       # Core parser module
├── app.py              # Flask web server
├── requirements.txt    # Python dependencies
├── start.bat           # Windows launcher script
├── static/
│   └── index.html      # Web interface
├── .cache/
│   └── game_data.json  # Cached extraction data
├── Season_1/           # Season 1 .rpy files
└── Season_2/           # Season 2 .rpy files
```

## Quick Start

### Prerequisites

- Python 3.10+

### Install dependencies

```bash
pip install -r requirements.txt
```

### Option 1: Web Interface (Recommended)

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

On Windows, you can also run:

```bat
start.bat
```

### Option 2: Command Line Extraction

```bash
python rpy_parser.py
```

This extracts data and caches it to `.cache/game_data.json`.

## API Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/data` | GET | Get all extracted game data |
| `/api/seasons` | GET | List available seasons |
| `/api/season/<season>` | GET | Get all scenes in a season |
| `/api/scene/<season>/<label>` | GET | Get specific scene data |
| `/api/labels` | GET | Get all labels with metadata |
| `/api/timeline` | GET | Get chronological scenes with reachability flags |
| `/api/search?q=<query>` | GET | Search dialogue |
| `/api/compare` | POST | Compare two scenes |
| `/api/playthrough/compare` | POST | Compare two multi-scene playthroughs |
| `/api/refresh` | POST | Force refresh cache |

## Cache Format

Data is cached in JSON format at `.cache/game_data.json`. The cache is automatically invalidated when .rpy files are added, removed, or modified (using MD5 hash validation).

## Usage Examples

### Review Full Story Streams

1. Open the app and let it auto-load all scenes from all chapters and seasons on both sides
2. Scroll through either stream to inspect scenes, choices, and conditions before comparing
3. Click option buttons inside each Choice block to set different branch paths per side

### Compare Playthroughs

1. Open the app and let it auto-load all scenes from all chapters and seasons on both sides
2. Pick different choice options in the left/right streams to create variable and branch differences
3. Click "Compare Playthroughs" to see a continuous line-by-line diff with change hunks
4. Click "Reload Full Story" if you want to reset both sides back to the full story list

### Refresh Data

1. Click "Refresh Data" in the top bar after changing source .rpy files
2. The app reloads extraction data and repopulates both full-story streams

## What Gets Extracted

✅ Character dialogue (e.g., `d "Hello there"`)
✅ Narrator text (e.g., `"The door creaks open."`)
✅ Menu choices and options
✅ Jump statements (scene transitions)
✅ Conditional blocks (if/elif/else)

❌ Variable assignments (`$ variable = value`)
❌ Define statements (`define character = ...`)
❌ Scene/Show/Hide commands
❌ Pause/With statements
❌ Comments

## Technical Details

- **Parser**: Custom regex-based parser for Ren'Py syntax
- **Cache**: JSON with MD5 hash validation
- **Backend**: Flask with CORS support
- **Frontend**: Vanilla JavaScript with modern CSS
- **Dependencies**: Flask + Flask-CORS

## Adding More Games

To use with other Ren'Py games:

1. Place .rpy files in a subdirectory
2. Update the season detection logic in `rpy_parser.py`
3. Run the extractor
