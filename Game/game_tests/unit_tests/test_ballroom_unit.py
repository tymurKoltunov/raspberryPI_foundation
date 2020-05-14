from Game.bin import *

def test_name_should_be_dininghall(ballroom):
    assert ballroom.name == ballroom_name, \
        f"name of dining hall is not 'Dining Hall', it is {dining_hall.name}"

def test_description_match(ballroom):
    assert ballroom.description == ballroom_description, \
        f"got: {ballroom.description}\nexpected: {ballroom_description}"

def test_inspection_should_match(ballroom):
    assert ballroom.inspect() == ballroom_inspect, \
        f"got: {ballroom.inspect()} \nexpected: {ballroom_inspect}"