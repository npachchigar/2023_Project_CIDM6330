import pytest
from allocation.domain.model import User

def test_create_user():
    user = User(username="john_doe", email="john_doe@example.com", password="password")
    assert user.username == "john_doe"
    assert user.email == "john_doe@example.com"
    assert user.password == "password"

def test_user_str():
    user = User(username="john_doe", email="john_doe@example.com", password="password")
    assert str(user) == "john_doe (john_doe@example.com)"

def test_user_repr():
    user = User(username="john_doe", email="john_doe@example.com", password="password")
    assert repr(user) == f"User(username='john_doe', email='john_doe@example.com', password='password')"