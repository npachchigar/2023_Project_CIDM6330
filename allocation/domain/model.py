from typing import List

class Song:
    def __init__(self, title: str, artist: str, album: str, genre: str, release_year: int):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.release_year = release_year

class Venue:
    def __init__(self, name: str, address: str, city: str, state: str, country: str):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country

class Information:
    def __init__(self, title: str, description: str , image_url: str):
        self.title = title
        self.description = description
        self.image_url = image_url

class Theater(Venue):
    def __init__(self, name: str, address: str, city: str, state: str, country: str):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country

class Event:
    def __init__(self, name: str, date: int, time: str, venue: str, theater: str, information: str):
        self.name = name
        self.date = date
        self.time = time
        self.venue = venue
        self.theater = theater
        self.information = information

class Artist:
    def __init__(self, id: str, name: str, genre: str, top_songs: List[Song]):
        self.id = id
        self.name = name
        self.genre = genre
        self.top_songs = top_songs

class Band:
    def __init__(self, band_id: str, name: str, genre: str):
        self.band_id = band_id
        self.name = name
        self.genre = genre        

class User:
    def __init__(self, id: str, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password