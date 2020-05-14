from Game.bin import *

def test_name_should_be_kitchen(kitchen):
    assert kitchen.name is kitchen_name, \
        f"name of kitchen is not 'Kitchen', it is {kitchen.name}"

def test_description_match(kitchen):
    assert kitchen.description is kitchen_description, \
        f"got: {kitchen.description}\nexpected: {kitchen_description}"

def test_inspection_should_match(kitchen):
    assert kitchen.inspect() is kitchen_inspect, \
        f"got: {kitchen.inspect()} \nexpected: {kitchen_inspect}"