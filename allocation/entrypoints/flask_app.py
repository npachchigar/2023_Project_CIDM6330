from flask import Flask, jsonify, request
from allocation.adapters.orm import start_mappers
from allocation.service_layer.service import SongService, VenueService, TheaterService, EventService, ArtistService, BandService, UserService

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Bolly Music Discovery App!"

@app.route('/songs')
def get_songs():
    song_service = SongService()
    songs = song_service.get_all_songs()
    return jsonify(songs)

@app.route('/venues')
def get_venues():
    venue_service = VenueService()
    venues = venue_service.get_all_venues()
    return jsonify(venues)

@app.route('/theaters')
def get_theaters():
    theater_service = TheaterService()
    theaters = theater_service.get_all_theaters()
    return jsonify(theaters)

@app.route('/events')
def get_events():
    event_service = EventService()
    events = event_service.get_all_events()
    return jsonify(events)

@app.route('/artists')
def get_artists():
    artist_service = ArtistService()
    artists = artist_service.get_all_artists()
    return jsonify(artists)

@app.route('/bands')
def get_bands():
    band_service = BandService()
    bands = band_service.get_all_bands()
    return jsonify(bands)

@app.route('/users')
def get_users():
    user_service = UserService()
    users = user_service.get_all_users()
    return jsonify(users)

if __name__ == '__main__':
    start_mappers()
    app.run(debug=True)