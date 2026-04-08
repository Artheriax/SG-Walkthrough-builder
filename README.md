# Summer's Gone Walkthrough Builder

Extract and compare Ren'Py dialogue/branching data from Summer's Gone scripts using a local Flask web app.

## Disclaimer

**I do not own the original .rpy source content in this repository.**
**Summer's Gone is created by OceanAVN:**
His links: https://allmylinks.com/ocean-avn

## What This Tool Does

- Parses Ren'Py files by label/scene context
- Extracts dialogue, narrator text, choices, jumps, calls, and condition flow
- Builds side-by-side playthrough streams for branch comparison
- Supports option selection per side to simulate variable/path differences
- Produces a continuous diff-style comparison across full playthroughs
- Caches parsed output for fast reloads

## Project Layout

```text
SG-Walkthrough-builder/
├── app.py                # Flask API + static UI server
├── rpy_parser.py         # Ren'Py parser and cache logic
├── rpy_cleaner.py        # Optional cleaner/helper script
├── requirements.txt      # Python dependencies
├── start.bat             # Windows one-click bootstrap launcher
├── static/
│   └── index.html        # Frontend UI
├── Season_1/             # Source scripts
└── Season_2/             # Source scripts
```

## Quick Start (Windows, One Click)

Run:

```bat
start.bat
```

The launcher will automatically:

1. Create .venv if it does not exist
2. Upgrade pip inside .venv
3. Install dependencies from requirements.txt
4. Start the Flask app
5. Auto-open the browser at http://localhost:5000

## Manual Start (Any Platform)

### Prerequisites

- Python 3.10+ (During Python installation turn on ``Add to PATH``)

### Setup and run

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000.

## App Controls

- Reload Full Story: reset both sides to the full stream
- Refresh Data: re-parse sources and refresh cached data
- Compare Playthroughs: run full diff between left and right branch selections

## API Endpoints

| Endpoint                    | Method | Purpose                          |
| --------------------------- | ------ | -------------------------------- |
| /api/data                   | GET    | Full extracted dataset           |
| /api/seasons                | GET    | List available seasons           |
| /api/season/<season>        | GET    | Scenes within a season           |
| /api/scene/<season>/<label> | GET    | Single scene payload             |
| /api/labels                 | GET    | Label metadata                   |
| /api/timeline               | GET    | Scene timeline with reachability |
| /api/search?q=<query>       | GET    | Dialogue search                  |
| /api/compare                | POST   | Compare two scenes               |
| /api/playthrough/compare    | POST   | Compare two playthrough streams  |
| /api/refresh                | POST   | Force full data refresh          |

## Auto-Open Browser Configuration

The app auto-opens the browser by default when started in debug mode.

- SG_AUTO_OPEN_BROWSER=0 disables auto-open
- SG_AUTO_OPEN_DELAY_SECONDS=1.0 controls launch delay

Examples (PowerShell):

```powershell
$env:SG_AUTO_OPEN_BROWSER="0"
python app.py
```

```powershell
$env:SG_AUTO_OPEN_DELAY_SECONDS="2.0"
python app.py
```

## Cache Behavior

- Cache file: .cache/game_data.json
- Invalidation: automatic when source file hashes change
- You can force refresh with the Refresh Data button or /api/refresh

## Extraction Coverage

Included:

- Character dialogue lines
- Narrator text lines
- Menu choices and option conditions
- Jump/call/call screen flow data
- If/elif/else condition tracking
- Scene state actions used by playthrough simulation

Not included as standalone narrative output:

- Most non-dialogue visual commands (scene/show/hide/with)
- Comments

## Troubleshooting

- If start.bat says Python is missing, install Python 3 and ensure py or python is on PATH.
- If port 5000 is in use, stop the other process or modify app.py port.
- If parsing seems stale, click Refresh Data or delete .cache/game_data.json.

## Notes for Adapting to Other Ren'Py Projects

1. Add your .rpy files in project subfolders.
2. Update source directory detection if needed.
3. Run the app and verify labels/scenes are discovered correctly.
4. I cannot 100% say this will work on every other project, because I made this specifically for games that were made in the way ``OceanAVN`` makes games.

## License

This repository uses a custom restricted license. See [LICENSE](LICENSE).

Policy summary:

- Allowed: personal use, local clone, and GitHub-native forks of this repository.
- Not allowed: mirrors/reuploads/redistribution outside the GitHub fork network rooted at this repository.
- Third-party Summer's Gone scripts/content remain owned by their original creator(s) and are not licensed by this repo.

