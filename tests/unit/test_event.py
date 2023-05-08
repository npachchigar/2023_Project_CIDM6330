import pytest
from allocation.domain.model import Event

def test_event_creation():
    # Test Event creation
    event = Event("Sufi Night", "2023-06-15", "Houston")
    assert event.name == "Sufi Night"
    assert event.date == "2023-06-15"
    assert event.venue == "Houston"