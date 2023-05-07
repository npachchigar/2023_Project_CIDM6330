from typing import List

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

    def get_songs(self) -> List[Song]:
        return self.session.query(Song).all()

    