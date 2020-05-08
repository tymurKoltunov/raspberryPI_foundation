from Game.bin import *

def test_name_should_be_kitchen(kitchen):
    assert kitchen.name == kitchen_name, f"name of kitchen is not 'Kitchen', it is {kitchen.name}"

def test_description_match(kitchen):
    assert kitchen.description == kitchen_description, f"got: {kitchen.description}\nexpected: {kitchen_description}"

def test_room_item_is_cheese(kitchen):
    assert isinstance(kitchen.item, type(Cheese())), "kitchen item is not of type 'Cheese'"

def test_inspection_should_match(kitchen):
    assert kitchen.inspect() == kitchen_inspect, f"got: {kitchen.inspect()} \nexpected: {kitchen_inspect}"