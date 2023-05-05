from typing import List

class Song:
    def __init__(self, title, artist, album, genre, length, release_year):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
        self.release_year = release_year

class Venue:
    def __init__(self, name, address, city, state, country):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country

class Information:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

class Theater:
    def __init__(self, name, address, city, state, country):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country

class Event:
    def __init__(self, name, date, time, venue, theater, information):
        self.name = name
        self.date = date
        self.time = time
        self.venue = venue
        self.theater = theater
        self.information = information

class Artist:
    def __init__(self, name, age, bio, genre, image_url):
        self.name = name
        self.age = age
        self.bio = bio
        self.genre = genre
        self.image_url = image_url

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password