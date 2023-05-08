import requests
import json
from allocation.entrypoints import create_app

def test_song_api(client):
    response = client.post('/songs', json={
        'title': 'Test Song',
        'artist': 'Test Artist',
        'album': 'Test Album',
        'year': 2023,
        'genre': 'Test Genre'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Song'

def test_event_api(client):
    response = client.post('/events', json={
        'title': 'Test Event',
        'date': '2023-06-01',
        'venue': 'Test Venue'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Event'

def test_theater_api(client):
    response = client.post('/theaters', json={
        'name': 'Test Theater',
        'location': 'Test Location'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Test Theater'

def test_artist_api(client):
    response = client.post('/artists', json={
        'name': 'Test Artist',
        'genre': 'Test Genre'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Test Artist'

def test_band_api(client):
    response = client.post('/bands', json={
        'name': 'Test Band',
        'genre': 'Test Genre'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Test Band'

def test_user_api(client):
    response = client.post('/users', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'test User'
    