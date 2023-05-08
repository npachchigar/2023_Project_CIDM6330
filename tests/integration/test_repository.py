import pytest
from allocation.adapters.repository import SongRepository

def test_song_repository():
    song_repo = SongRepository()
    
    song = song_repo.create(title="Example Song", artist="Example Artist")
    
    assert song.id is not None
    
    retrieved_song = song_repo.get_by_id(song.id)
    
    assert retrieved_song.title == song.title
    assert retrieved_song.artist == song.artist
    
    song.title = "Updated Song"
    song.artist = "Updated Artist"
    
    updated_song = song_repo.update(song)
    
    assert updated_song.title == "Updated Song"
    assert updated_song.artist == "Updated Artist"
    
    