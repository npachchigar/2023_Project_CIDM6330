import pytest
from allocation.entrypoints import create_app
from allocation.entrypoints import get_db, init_db

# Set up the app for testing
@pytest.fixture(scope='session')
def app():
    app = create_app({'TESTING': True, 'DATABASE': 'test.db'})
    with app.app_context():
        init_db()
    yield app
    with app.app_context():
        db = get_db()
        db.execute('DELETE FROM users')
        db.execute('DELETE FROM bands')
        db.execute('DELETE FROM artists')
        db.execute('DELETE FROM theaters')
        db.execute('DELETE FROM events')
        db.execute('DELETE FROM songs')
        db.execute('DELETE FROM venues')
        db.commit()

# Set up the client to make API requests
@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

# Set up a test database
@pytest.fixture(scope='session')
def db(app):
    with app.app_context():
        db = get_db()
        yield db
        db.execute('DELETE FROM users')
        db.execute('DELETE FROM bands')
        db.execute('DELETE FROM artists')
        db.execute('DELETE FROM theaters')
        db.execute('DELETE FROM events')
        db.execute('DELETE FROM songs')
        db.execute('DELETE FROM venues')
        db.commit()

# Set up a test ORM object
@pytest.fixture(scope='session')
def orm(db):
    from allocation.adapters.orm import ORM
    return ORM(db)

# Set up a test repository object
@pytest.fixture(scope='session')
def repo(orm):
    from allocation.adapters.repository import Repository
    return Repository(orm)


