import pytest
from allocation.domain.model import Theater

def test_theater_creation():
    # Test Theater creation
    theater = Theater("Test Cinema", "Houston")
    assert theater.name == "Test Cinema"
    assert theater.location == "Houston"