from flask import Flask, jsonify, request
from allocation.service_layer.service import AllocationService
from allocation.domain.model import Song, Venue, Information, Theater, Event, Artist, Band, User
from flask_sqlalchemy import SQLAlchemy
from allocation.adapters.orm import start_mappers

app = Flask(__name__)
db = SQLAlchemy()
# Initialize the service
service = AllocationService()

@app.route('/')
def index():
    return "Welcome to the Bolly Music Discovery App!"

@app.route('/song', methods=['POST'])
def add_song():
    # Parse the request body
    data = request.json
    name = data['name']
    duration = data['duration']
    artist = data['artist']
    album = data['album']

    # Create a new song object
    song = Song(name=name, duration=duration, artist=artist, album=album)

    # Call the allocation service to add the song
    service.add_song(song)

    # Return the response
    return jsonify({'success': True, 'message': 'Song added successfully.'})

@app.route('/venue', methods=['POST'])
def add_venue():
    # Parse the request body
    data = request.json
    name = data['name']
    location = data['location']
    capacity = data['capacity']

    # Create a new venue object
    venue = Venue(name=name, location=location, capacity=capacity)

    # Call the allocation service to add the venue
    service.add_venue(venue)

    # Return the response
    return jsonify({'success': True, 'message': 'Venue added successfully.'})

@app.route('/information', methods=['POST'])
def add_information():
    # Parse the request body
    data = request.json
    title = data['title']
    description = data['description']

    # Create a new information object
    information = Information(title=title, description=description)

    # Call the allocation service to add the information
    service.add_information(information)

    # Return the response
    return jsonify({'success': True, 'message': 'Information added successfully.'})

@app.route('/theater', methods=['POST'])
def add_theater():
    # Parse the request body
    data = request.json
    name = data['name']
    location = data['location']
    capacity = data['capacity']

    # Create a new venue object
    theater = Theater(name=name, location=location, capacity=capacity)

    # Call the allocation service to add the venue
    service.add_venue(theater)

    # Return the response
    return jsonify({'success': True, 'message': 'Theater added successfully.'})


def create_app():
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    start_mappers()
    app.run(debug=True)