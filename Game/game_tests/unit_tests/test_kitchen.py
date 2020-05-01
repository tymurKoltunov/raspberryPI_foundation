import pytest
from Game.bin.room import *

@pytest.fixture
def kitchen():
    return Kitchen()

def test_name_should_be_kitchen(kitchen):
    assert kitchen.name == "Kitchen"