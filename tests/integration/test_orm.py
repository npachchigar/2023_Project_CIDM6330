import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from allocation.domain.model import Song, Venue, Information, Theater, Artist, Band, User

def test_orm_song():
    # Test ORM for Song model
    engine = create_engine('sqlite:///test.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    song = Song("Chaiyya Chaiyya", "Sukhwinder Singh")
    session.add(song)
    session.commit()
    
    query = session.query(Song).filter_by(title='Chaiyya Chaiyya')
    assert query.count() == 1
    
    session.delete(song)
    session.commit()
    query = session.query(Song).filter_by(title='Chaiyya Chaiyya')
    assert query.count() == 0