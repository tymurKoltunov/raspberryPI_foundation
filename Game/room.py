from item import *
from character import *


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
        print("The " + self.name + "\n" + "-" * 20)
        for direction in self.linked_rooms:
            print("The " + self.linked_rooms[direction].name + " is " + direction)

    def inspect(self):
        print("Looking around")


class Kitchen(Room):
    item = Cheese()

    def __init__(self):
        super().__init__()
        self.name = 'Kitchen'
        self.description = "A dank and dirty room buzzing with flies."

    def inspect(self):
        print(
            "Looks completely abandoned, except for the big piece of nice looking Cheese on the table. Flies avoid it for some reason.")


class DiningHall(Room):
    character = Dave()

    def __init__(self):
        super().__init__()
        self.name = "Dining Hall"
        self.description = "About twice as big as kitchen, with big table in the middle and some scattered chairs. looks completely abandoned."

    def inspect(self):
        print("Nothing of value can be found here. Only dust and damaged furniture")


class Ballroom(Room):
    character = Elsa()
    def __init__(self):
        super().__init__()
        self.name = "Ballroom"
        self.description = "Big room with an even bigger window, which hasn't been washed for a long time, fills room  with grey light."

    def inspect(self):
        print("Looks like someone took everything out of this room")
