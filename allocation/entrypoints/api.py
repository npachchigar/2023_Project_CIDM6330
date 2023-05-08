from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/songs')
def get_songs():
    return jsonify({'songs': []})

@api_bp.route('/venues')
def get_venues():
    return jsonify({'venues': []})

@api_bp.route('/theaters')
def get_theaters():
    return jsonify({'theaters': []})

@api_bp.route('/events')
def get_events():
    return jsonify({'events': []})

@api_bp.route('/artists')
def get_artists():
    return jsonify({'artists': []})

@api_bp.route('/users')
def get_users():
    return jsonify({'users': []})