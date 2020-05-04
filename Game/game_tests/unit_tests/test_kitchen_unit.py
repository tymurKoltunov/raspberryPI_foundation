import pytest
from Game.bin.room import *
from Game.bin.item import Cheese


def test_name_should_be_kitchen(kitchen):
    assert kitchen.name == "Kitchen"

def test_description_match(kitchen):
    assert kitchen.description == "A dank and dirty room buzzing with flies."

def test_room_item_is_cheese(kitchen):
    assert isinstance(kitchen.item, type(Cheese()))

def test_inspection_should_match(kitchen):
    assert kitchen.inspect() == "Looks completely abandoned, except for the big piece of nice looking Cheese on the table. Flies avoid it for some reason."