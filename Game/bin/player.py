from .character import *


class Player:
    def __init__(self, current_pos, name='defalut'):
        self.name = name
        self.location = current_pos
        self.backpack = {}
        self.equipped = {"Head": None,
                         "Accessory": None,
                         "Torso": None,
                         "Hands": None,
                         "Legs": None,
                         "Feet": None,
                         "Weapon": None}

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @location.setter
    def location(self, location):
        self._location = location

    def talk(self):
        if self.location.character:
            return self.location.character.talk()
        else:
            return "There is no one to talk to."

    def fight(self):
        if self.location.character is None:
            return "There is no one to fight here."
        if isinstance(self.location.character, Friend):
            return self.location.characer.fight('friend')
        weapon = input("What will you use as a weapon? \n")
        if weapon in self.backpack:
            fight_result = self.location.characer.fight(self.backpack[weapon])
            if "fend" in fight_result:
                self.location.character = None
            return fight_result
        else:
            return "You don't have this."

    def move(self, direction):
        if direction in self.location.linked_rooms:
            self.location = self.location.linked_rooms[direction]
            return f"You have moved {direction}."
        else:
            return "No way"

    def take(self):
        if self.location.item:
            self.backpack[self.location.item.name] = self.location.item
            item_name = self.location.item.name
            self.location.item = None
            return f"You took {item_name}. And put it in your backpack."
        else:
            return "There is nothing to take."

    def check_backpack(self):
        if self.backpack:
            for item in self.backpack:
                return self.backpack[item].name + " " + self.backpack[item].description + "\n"
        else:
            return "You have nothing in your backpack."

    def check_equipped(self):
        equipped_str = ""
        for body_part, item in self.equipped.items():
            if item is None:
                equipped_str += f"On {body_part} slot you have equipped nothing"
            else:
                equipped_str += f"On {body_part} slot you have equipped {item}"
        return equipped_str

    def equip(self, item):
        item_class = item.__class__.__name__
        if item_class in self.equipped:
            self.equipped[item_class] = item
            return f"You have equipped {item.name} on {item_class} item slot"
