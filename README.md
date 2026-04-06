# Summer's Gone Walkthrough Builder

A modern, modular tool for extracting and comparing dialogue from Ren'Py visual novel files (.rpy). Built specifically for "Summer's Gone" Season 1 & 2.

## Features

- **Scene-Aware Extraction**: Properly tracks labels and jumps to maintain scene context
- **Dialogue Extraction**: Extracts all character dialogue and narrator text
- **Choice Tracking**: Captures all menu choices with their conditions
- **Condition Tracking**: Tracks if/elif/else conditions that affect dialogue
- **Jump Detection**: Identifies scene transitions via jump statements
- **Smart Caching**: Uses JSON cache with file hash validation for fast reloads
- **Web Interface**: Modern, dark-themed UI for browsing and comparing scenes
- **Comparison Tool**: Compare dialogue between different scenes/playthroughs
- **Search**: Full-text search across all dialogue

## Project Structure

```
/workspace/
├── rpy_parser.py       # Core parser module
├── app.py              # Flask web server
├── static/
│   └── index.html      # Web interface
├── .cache/
│   └── game_data.json  # Cached extraction data
├── Season_1/           # Season 1 .rpy files
└── Season_2/           # Season 2 .rpy files
```

## Quick Start

### Option 1: Web Interface (Recommended)

```bash
cd /workspace
python app.py
```

Then open http://localhost:5000 in your browser.

### Option 2: Command Line Extraction

```bash
cd /workspace
python rpy_parser.py
```

This extracts data and caches it to `.cache/game_data.json`.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/data` | GET | Get all extracted game data |
| `/api/seasons` | GET | List available seasons |
| `/api/season/<season>` | GET | Get all scenes in a season |
| `/api/scene/<season>/<label>` | GET | Get specific scene data |
| `/api/labels` | GET | Get all labels with metadata |
| `/api/search?q=<query>` | GET | Search dialogue |
| `/api/compare` | POST | Compare two scenes |
| `/api/refresh` | POST | Force refresh cache |

## Cache Format

Data is cached in JSON format at `.cache/game_data.json`. The cache is automatically invalidated when any .rpy file changes (using MD5 hash validation).

## Usage Examples

### Browse Scenes
1. Select a season from the sidebar
2. Click on any scene to view its contents
3. See dialogues, choices, and jump targets

### Compare Playthroughs
1. Select Scene 1 from the compare panel
2. Select Scene 2 from the compare panel
3. Click "Compare" to see differences

### Search Dialogue
1. Type a search term in the search box
2. Press Enter or click the search button
3. Click "View Scene" on any result to navigate

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
- **No external dependencies** beyond Flask

## Adding More Games

To use with other Ren'Py games:
1. Place .rpy files in a subdirectory
2. Update the season detection logic in `rpy_parser.py`
3. Run the extractor
