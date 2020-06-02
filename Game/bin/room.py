from .item import *
from .character import *
from .data import *


class Room:
    """
    Description
    -----------
    Represents a single room location of the game mansion.

    Instance variables
    ------------------
    name: str
        room name
    description: str
        room description
    inspect: str
        detailed room description
    item: Item
        item located in the room
        (default is empty Item object)
    character: Character
        character located in the room
        (default is empty Character object)
    exit: bool
        boolean value that indicates the room where player can finish the game

    Instance methods
    ----------------
    link_room(self, room_to_link: 'Room', direction: str)
        populates linked_rooms  dictionary, direction parameter is key, room_to_link is value
    get_details()
        Prints room name and description, keys and values name attributes of linked rooms dictionary
    inspect()
        Returns inspect instance variable
    """
    def __init__(self, name: str, description: str, inspect: str, item=Item, character=Character, exit=False):
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

    def link_room(self, room_to_link: 'Room', direction: str):
        """
        Parameter
        ---------
        room_to_link: 'Room'
            Room object to be added to linked_rooms dictionary as value
        direction: str
            direction in which linked room will exist, added to linked_rooms dictionary as key
        Description
        ----------
        By linking rooms game mansion is created. Each room knows only about rooms that are next to it
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """
        Description
        -----------
        Prints room name and description, keys and values name attributes of linked rooms dictionary
        """
        print("The " + self.name + "\n" + f"{self.description}" + "\n" + "-" * 20)
        for direction in self.linked_rooms:
            print(f"The {self.linked_rooms[direction].name} is {direction}")

    def inspect(self):
        """
        Description
        -----------
        Returns inspect instance variable
        """
        return self.inspect
