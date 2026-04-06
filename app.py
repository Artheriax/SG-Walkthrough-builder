"""
Web-based Walkthrough Builder for Ren'Py games.
Provides a Flask API and serves a modern React-like frontend for comparing playthroughs.
"""

import os
import json
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from rpy_parser import extract_game_data, CacheManager, RPyParser

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Global cache for game data
game_data = None
cache_manager = CacheManager()
parser = RPyParser()


def get_game_data():
    """Load or extract game data."""
    global game_data
    if game_data is None:
        if cache_manager.is_cache_valid(parser, 'Season_1'):
            print("Loading cached data...")
            game_data = cache_manager.load()
        else:
            print("Extracting game data...")
            game_data = extract_game_data(['Season_1', 'Season_2'])
    return game_data


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
    return jsonify(list(data['seasons'].keys()))


@app.route('/api/season/<season>', methods=['GET'])
def get_season_scenes(season):
    """Get all scenes for a specific season."""
    data = get_game_data()
    if season in data['seasons']:
        return jsonify(data['seasons'][season])
    return jsonify({}), 404


@app.route('/api/scene/<season>/<label_name>', methods=['GET'])
def get_scene(season, label_name):
    """Get a specific scene's data."""
    data = get_game_data()
    if season in data['seasons'] and label_name in data['seasons'][season]:
        return jsonify(data['seasons'][season][label_name])
    return jsonify({}), 404


@app.route('/api/labels', methods=['GET'])
def get_all_labels():
    """Get all labels with their metadata."""
    data = get_game_data()
    return jsonify(data['labels'])


@app.route('/api/search', methods=['GET'])
def search_dialogue():
    """Search for dialogue containing specific text."""
    query = request.args.get('q', '').lower()
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
    req_data = request.json
    season1 = req_data.get('season1')
    label1 = req_data.get('label1')
    season2 = req_data.get('season2')
    label2 = req_data.get('label2')
    
    data = get_game_data()
    
    scene1 = data['seasons'].get(season1, {}).get(label1, {})
    scene2 = data['seasons'].get(season2, {}).get(label2, {})
    
    dialogues1 = {d['text']: d for d in scene1.get('dialogues', [])}
    dialogues2 = {d['text']: d for d in scene2.get('dialogues', [])}
    
    # Find differences
    only_in_1 = [d for text, d in dialogues1.items() if text not in dialogues2]
    only_in_2 = [d for text, d in dialogues2.items() if text not in dialogues1]
    common = [d for text, d in dialogues1.items() if text in dialogues2]
    
    return jsonify({
        'only_in_first': only_in_1,
        'only_in_second': only_in_2,
        'common': common,
        'scene1_info': {'season': season1, 'label': label1, 'total_dialogues': len(dialogues1)},
        'scene2_info': {'season': season2, 'label': label2, 'total_dialogues': len(dialogues2)}
    })


@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """Force refresh of game data (invalidate cache)."""
    global game_data
    game_data = None
    game_data = extract_game_data(['Season_1', 'Season_2'])
    return jsonify({'status': 'refreshed', 'labels': len(game_data['labels'])})


if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    print("Starting Walkthrough Builder server...")
    print("Open http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=True)
