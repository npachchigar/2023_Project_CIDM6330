import pytest
from allocation.domain.model import Song

def test_create_song():
    song = Song(title="Tum Hi Ho", artist="Arijit Singh", duration=5.5)
    assert song.title == "Tum Hi Ho"
    assert song.artist == "Arijit Singh"
    assert song.duration == 5.5