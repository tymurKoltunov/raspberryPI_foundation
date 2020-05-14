from Game.bin import *

def test_name_should_be_dininghall(dining_hall):
    assert dining_hall.name is dining_hall_name, \
        f"name of dining hall is not 'Dining Hall', it is {dining_hall.name}"

def test_description_match(dining_hall):
    assert dining_hall.description is dining_hall_description, \
        f"got: {dining_hall.description}\nexpected: {dining_hall_description}"

def test_inspection_should_match(dining_hall):
    assert dining_hall.inspect() is dining_hall_inspect, \
        f"got: {dining_hall.inspect()} \nexpected: {dining_hall_inspect}"

def test_character_should_be_dave(dining_hall):
    assert dining_hall.character.name is "Dave", \
        f"got: {dining_hall.character.name} \nexpected: 'Dave'"