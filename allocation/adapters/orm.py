from typing import List

from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey

from allocation.domain.model import (
    Song, Venue, Theater, Event, Artist, Band, User
)

metadata = MetaData()

songs = Table(
    "songs",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String),
    Column("artist_id", ForeignKey("artists.id"))
)

venues = Table(
    "venues",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("location", String),
    Column("capacity", Integer)
)

theaters = Table(
    "theaters",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("location", String),
    Column("capacity", Integer)
)

events = Table(
    "events",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("venue_id", ForeignKey("venues.id")),
    Column("theater_id", ForeignKey("theaters.id"))
)

artists = Table(
    "artists",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("description", String)
)

bands = Table(
    "bands",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("description", String),
    Column("leader_id", ForeignKey("artists.id")),
    Column("members", String)
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String),
    Column("email", String),
    Column("password", String)
)

mapper(Song, songs, properties={
    "artist": relationship(Artist, backref="songs")
})

mapper(Venue, venues, properties={
    "events": relationship(Event, backref="venue")
})

mapper(Theater, theaters, properties={
    "events": relationship(Event, backref="theater")
})

mapper(Event, events)

mapper(Artist, artists, properties={
    "bands": relationship(Band, backref="leader")
})

mapper(Band, bands, properties={
    "leader": relationship(Artist, backref="bands")
})

mapper(User, users)