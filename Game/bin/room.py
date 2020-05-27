from .item import *
from .character import *
from .data import *


class Room:

    def __init__(self, name: str, description: str, inspect: str, item= Item, character=Character, exit=False):
        self.name = name
        self.description = description
        self.linked_rooms = {}
        self.inspect = inspect
        self.item = item
        self.character = character
        self.exit = exit

    @property
    def character(self):
        return self._character

    @property
    def item(self):
        return self._item

    @property
    def name(self):
        return self._name

    @property
    def inspect(self):
        return self._inspect

    @property
    def description(self):
        return self._description

    @character.setter
    def character(self, character):
        self._character = character

    @item.setter
    def item(self, item):
        self._item = item

    @name.setter
    def name(self, name):
        self._name = name

    @inspect.setter
    def inspect(self, inspect):
        self._inspect = inspect

    @description.setter
    def description(self, desc):
        self._description = desc

    def link_room(self, room_to_link, direction: str):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("The " + self.name + "\n" + f"{self.description}" + "\n" + "-" * 20)
        for direction in self.linked_rooms:
            print(f"The {self.linked_rooms[direction].name} is {direction}")

    def inspect(self):
        return self.inspect

