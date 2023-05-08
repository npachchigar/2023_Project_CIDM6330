import pytest
from allocation.domain.model import Artist

def test_artist_creation():
    # Test Artist creation
    artist = Artist("Arijit Singh", "arijit@gmail.com")
    assert artist.name == "Arijit Singh"
    assert artist.email == "arijit@gmail.com"