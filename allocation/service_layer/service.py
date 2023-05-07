from allocation.domain import model
from allocation.adapters import repository
from allocation.adapters.orm import start_mappers

def allocate(event_id: str, venue_id: str, event_date: str, tickets: int,
             artist_name: str, user_id: str, information: str):
    start_mappers()
    batch_ref = model.Batch.allocate(event_id, venue_id, event_date, tickets)
    artist = repository.ArtistRepository.find_by_name(artist_name)
    user = repository.UserRepository.get(user_id)
    venue = repository.VenueRepository.get(venue_id)
    event = repository.EventRepository.get(event_id)
    information = model.Information(information)
    artist.events.add(event)
    batch = repository.BatchRepository.get(batch_ref)
    return batch.reference

def add_artist(name: str):
    start_mappers()
    artist = model.Artist(name)
    repository.ArtistRepository.add(artist)
    
def get_artist(artist_id: str):
    start_mappers()
    artist = repository.ArtistRepository.get(artist_id)
    return artist

def add_venue(name: str, location: str):
    start_mappers()
    venue = model.Venue(name, location)
    repository.VenueRepository.add(venue)
    
def get_venue(venue_id: str):
    start_mappers()
    venue = repository.VenueRepository.get(venue_id)
    return venue

def add_information(content: str):
    start_mappers()
    information = model.Information(content)
    repository.InformationRepository.add(information)
    
def get_information(information_id: str):
    start_mappers()
    information = repository.InformationRepository.get(information_id)
    return information

def add_theater(name: str, location: str):
    start_mappers()
    theater = model.Theater(name, location)
    repository.TheaterRepository.add(theater)
    
def get_theater(theater_id: str):
    start_mappers()
    theater = repository.TheaterRepository.get(theater_id)
    return theater

def add_event(event_date: str, venue_id: str, theater_id: str, information_id: str):
    start_mappers()
    venue = repository.VenueRepository.get(venue_id)
    theater = repository.TheaterRepository.get(theater_id)
    information = repository.InformationRepository.get(information_id)
    event = model.Event(event_date, venue, theater, information)
    repository.EventRepository.add(event)
    
def get_event(event_id: str):
    start_mappers()
    event = repository.EventRepository.get(event_id)
    return event

def add_user(name: str, email: str):
    start_mappers()
    user = model.User(name, email)
    repository.UserRepository.add(user)
    
def get_user(user_id: str):
    start_mappers()
    user = repository.UserRepository.get(user_id)
    return user