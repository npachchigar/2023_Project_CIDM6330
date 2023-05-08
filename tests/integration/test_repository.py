import pytest
from allocation.adapters.repository import SongRepository, EventRepository, BandRepository, InformationRepository, UserRepository

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


def test_event_repository():
    event_repo = EventRepository()
    
    event = event_repo.create(title="Example Event", artist="Example Artist", band="Example Band")
    
    assert event.name is not None
    
    retrieved_event = event_repo.get_by_name(event.name)
    
    assert retrieved_event.title == event.title
    assert retrieved_event.artist == event.artist
    assert retrieved_event.band == event.band
    
    event.title = "Updated event"
    event.artist = "Updated Artist"
    event.band = "Updated band"
    
    updated_event = event_repo.update(event)
    
    assert updated_event.title == "Updated event"
    assert updated_event.artist == "Updated Artist"
    assert updated_event.band == "Updated band" 
    

def test_band_repository():
    band_repo = BandRepository()
    
    band = band_repo.create(title="Example band", artist="Example Artist", event="Example event")
    
    assert band.name is not None
    
    retrieved_band = band_repo.get_by_name(band.name)
    
    assert retrieved_band.title == band.title
    assert retrieved_band.artist == band.artist
    assert retrieved_band.event == band.event
    
    band.title = "Updated title"
    band.artist = "Updated Artist"
    band.event = "Updated event"
    
    updated_band = band_repo.update(band)
    
    assert updated_band.title == "Updated title"
    assert updated_band.artist == "Updated Artist"
    assert updated_band.event == "Updated event"

def test_information_repository():
    information_repo = InformationRepository()
    
    information = information_repo.create(artist="Example Artist", event="Example event", band="Example band", theater="Example theater")
    
    assert information.name is not None
    
    retrieved_information = information_repo.get_by_name(information.name)
    
    assert retrieved_information.band == information.band
    assert retrieved_information.artist == information.artist
    assert retrieved_information.event == information.event
    assert retrieved_information.theater == information.theater
    
    information.band = "Updated band"
    information.artist = "Updated Artist"
    information.event = "Updated event"
    information.theater = "Updated theater"
    
    updated_information = information_repo.update(information)
    
    assert updated_information.band == "Updated bandt"
    assert updated_information.artist == "Updated Artist"
    assert updated_information.event == "Updated event"    
    assert updated_information.theater == "Updated theater"


def test_user_repository():
    user_repo = UserRepository()
    
    user = user_repo.create(name="Example name", password="Example password")
    
    assert user.name is not None
    
    retrieved_user = user_repo.get_by_name(user.name)
    
    assert retrieved_user.name == user.name
    assert retrieved_user.password == user.password
    
    user.name = "Updated name"
       
    updated_user = user_repo.update(user)
    
    assert updated_user.name == "Updated name"
    assert updated_user.password == "Updated password"   