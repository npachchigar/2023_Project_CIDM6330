import requests
from allocation.adapters.orm import SongORM
from allocation.service_layer.service import SongService

def test_can_create_a_song_through_the_api():
    service = SongService()
    data = {"title": "Tum Hi Ho", "artist": "Arijit Singh", "duration": 5.5}
    response = requests.post("http://localhost:5000/songs", json=data)

    assert response.status_code == 201
    song_id = response.json()["id"]

    with session_scope() as session:
        song = session.query(SongORM).get(song_id)
        assert song.title == "Tum Hi Ho"
        assert song.artist == "Arijit Singh"
        assert song.duration == 5.5