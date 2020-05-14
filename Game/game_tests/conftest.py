import pytest
from Game.bin import *


@pytest.fixture(scope="module")
def kitchen():
    return create_rooms()


@pytest.fixture(scope="module")
def dining_hall():
    return create_rooms("dining_hall")


@pytest.fixture(scope="module")
def ballroom():
    return create_rooms("ballroom")