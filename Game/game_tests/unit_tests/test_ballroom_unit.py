from Game.bin import *

def test_name_should_be_dininghall(ballroom):
    assert ballroom.name is ballroom_name, \
        f"got {ballroom.name} \nexpected {ballroom_name}"

def test_description_match(ballroom):
    assert ballroom.description is ballroom_description, \
        f"got: {ballroom.description}\nexpected: {ballroom_description}"

def test_inspection_should_match(ballroom):
    assert ballroom.inspect() is ballroom_inspect, \
        f"got: {ballroom.inspect()} \nexpected: {ballroom_inspect}"

def test_character_should_be_elsa(ballroom):
    assert ballroom.character.name is "Elsa", \
        f"got: {ballroom.character.name} \nexpected: 'Elsa'"