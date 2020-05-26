from .character import *


class Player:
    health = 3
    strength = 0

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
        health_lost = self.location.character.fight(Player.strength)
        if health_lost >= Player.health:
            return f"{self.location.character.name} crushes you, puny adventurer\n"
        else:
            Player.health -= health_lost
            defeated_char_name = self.location.character.name
            self.location.character = None
            if self.equipped['Weapon'] is None:
                return f"You killed {defeated_char_name} with Unarmed and lost" \
                       f" {health_lost} health. Your current health is {Player.health}"
            return f"You killed {defeated_char_name}" \
                   f"with {self.equipped['Weapon'].name} and lost {health_lost} health. " \
                   f"Your current health is {Player.health}"

    def move(self, direction):
        if direction in self.location.linked_rooms:
            self.location = self.location.linked_rooms[direction]
            return f"You have moved {direction}"
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
            list_of_items =""
            for item in self.backpack:
                list_of_items += ">" + self.backpack[item].name + "\n" + \
                       self.backpack[item].description + "\n" + \
                       self.backpack[item].usage + "\n"
            return list_of_items
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

    def equip(self):

        item_name = input("What item do you want to equip?\n>")
        if item_name in self.backpack:
            item = self.backpack[item_name]
        else:
            return "You don't have this"
        if item.type in self.equipped:
            self.equipped[item.type] = item
            if item.type == "Weapon":
                Player.strength = item.strength
            return f"You have equipped {item.name} on {item.type} item slot"
        else:
            return "You can not equip this"

    def give(self):
        if self.location.character:
            item = input(f"What do you want to give to {self.location.character.name}?\n>")
            if item in self.backpack:
                if self.location.character.give(item):
                    if isinstance(self.location.character, Friend):
                        self.backpack[self.location.character.possession.name] = \
                            self.location.character.possession
                        loot = self.location.character.possession.name
                        self.location.character.treat = None
                        self.location.character.possession = None
                        del self.backpack[item]
                        return f"{self.location.character.name} accepted your gift, and gave you {loot}"
                    if isinstance(self.location.character, Enemy):
                        name = self.location.character.name
                        self.location.character = None
                        del self.backpack[item]
                        return f"You fend off {name} with {item}"
                    else:
                        return f"It does not accept {item}"
                else:
                    return f"{self.location.character.name} does not like {item}"
            else:
                return "You don't have this"
        else:
            return "There is no one here"