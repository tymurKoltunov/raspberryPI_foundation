from .item import *
from .character import *
from .data import *

class Room:
    character = None
    item = None

    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.linked_rooms = {}

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("The " + self.name + "\n" + f"{self.description}" + "\n" + "-" * 20)
        for direction in self.linked_rooms:
            print(f"The {self.linked_rooms[direction].name} is {direction}")

    def inspect(self):
        return "Looking around"


class Kitchen(Room):
    def __init__(self):
        super().__init__()
        self.name = kitchen_name
        self.description = kitchen_description

    def inspect(self):
        return kitchen_inspect


class DiningHall(Room):

    def __init__(self):
        super().__init__()
        self.name = dining_hall_name
        self.description = dining_hall_description

    def inspect(self):
        return dining_hall_inspect


class Ballroom(Room):

    def __init__(self):
        super().__init__()
        self.name = ballroom_name
        self.description = ballroom_description

    def inspect(self):
        return ballroom_inspect
