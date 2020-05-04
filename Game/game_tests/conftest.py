import pytest
from Game.bin.room import *
from Game.bin.player import *

@pytest.fixture
def kitchen():
    return Kitchen()

@pytest.fixture
def player(position):
    return Player(position)