from typing import List
from allocation.domain import model
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from allocation.domain.model import (
    Song, Venue, Theater, Event, Artist, Band, User
)
from allocation.domain import repository


class SqlAlchemyRepository(repository.AbstractRepository):

    def __init__(self, session: Session):
        self.session = session

    def add(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise repository.IntegrityError

    def get(self, id):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError

    def search(self, filters):
        raise NotImplementedError

    def update(self, model):
        raise NotImplementedError

    def get_song(session: Session, title: str) -> model.Song:
        return session.query(model.Song).filter_by(title=title).first()


    def add_song(session: Session, song: model.Song):
        session.add(song)
        session.commit()


    def get_venue(session: Session, name: str) -> model.Venue:
        return session.query(model.Venue).filter_by(name=name).first()


    def add_venue(session: Session, venue: model.Venue):
        session.add(venue)
        session.commit()


    def get_theater(session: Session, name: str) -> model.Theater:
        return session.query(model.Theater).filter_by(name=name).first()


    def add_theater(session: Session, theater: model.Theater):
        session.add(theater)
        session.commit()


    def get_event(session: Session, name: str) -> model.Event:
        return session.query(model.Event).filter_by(name=name).first()


    def add_event(session: Session, event: model.Event):
        session.add(event)
        session.commit()


    def get_artist(session: Session, name: str) -> model.Artist:
        return session.query(model.Artist).filter_by(name=name).first()


    def add_artist(session: Session, artist: model.Artist):
        session.add(artist)
        session.commit()


    def get_user(session: Session, username: str) -> model.User:
        return session.query(model.User).filter_by(username=username).first()


    def add_user(session: Session, user: model.User):
        session.add(user)
        session.commit()

    