from .character import *
from .room import *


class Player:
    """
    Player class that interacts with the world.

    Attributes
    ----------
    name : str
        name of the player
    health : int
        health of the player(default 3)
    strength : int
        strength of the player, influences result of a fight
    location: Room
        current room in which player is located
    backpack : dict
        dictionary which contains items that player picks up during game. Key is the name of the item and value is Item object
    equipped : dict
        dictionary which contains players equipped items. Key is body part(item type) value is Item object

    Methods
    -------
    talk()
        talks to character in current room
    fight()
        fights with a character in current room
    move(direction : str)
        changes current room to the one that in the direction string passed if the direction is correct and room there exists
    take()
        puts the item in current room to backpack and removes this item from room
    check_backpack()
        returns string with name, description and usage of each item in backpack dictionary
    check_equipped()
        returns string with name, description and usage of each item in equipped dictionary
    equip()
        adds item to equipped dictionary
    give()
        gives an item to character in current room
    use()
        uses an item
    """

    def __init__(self, current_pos: Room, name='defalut'):
        self.name = name
        self.health = 3
        self.strength = 0
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
    def strength(self):
        return self._strength

    @property
    def health(self):
        return self._health

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @health.setter
    def health(self, health):
        self._health = health

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    @name.setter
    def name(self, name):
        self._name = name

    @location.setter
    def location(self, location):
        self._location = location

    def talk(self):
        """
        Returns talk string from character in current location
        If no character in current location is found, "There is no one to talk to." string is returned
        """
        if self.location.character:
            return self.location.character.talk()
        else:
            return "There is no one to talk to."

    def fight(self):
        """
        Description
        -----------
        Checks if there is a character to fight in current location
            If there is none, "There is no one to fight here." string is returned
        Checks if character is Friend
            If Friend, returns result of Friend class fight() method
        Calls fight() method from Enemy class and passes current strength attribute to it
        Checks if lethal damage was received
            If lethal damage was received, "char_name crushes you, puny adventurer" string is returned
        If there is any loot in character, puts loot in backpack and places None value to loot attribute in that character
            Adds info about loot to returned value
        Puts None to character attribute of current location
        Returns string with information about fight result, health lost, health left and loot info(if any)
        """

        returned_string = "You killed {defeated_char_name}" \
                          "with {Weapon} and lost {health_lost} health. " \
                          "Your current health is {health_curr}"
        if self.location.character is None:
            return "There is no one to fight here."
        if isinstance(self.location.character, Friend):
            return self.location.characer.fight('friend')
        health_lost = self.location.character.fight(self.strength)
        if health_lost >= self.health:
            return f"{self.location.character.name} crushes you, puny adventurer\n"
        else:
            self.health -= health_lost
            defeated_char_name = self.location.character.name
            if self.location.character.loot.name:
                returned_string += f"You looted {self.location.character.loot.name} from {self.location.character.name}"
                self.backpack[self.location.character.loot.name] = self.location.character.loot
                self.location.character.loot = None
            self.location.character = None
            if self.equipped['Weapon'] is None:
                return returned_string.format(defeated_char_name=defeated_char_name,
                                              weapon="Unarmed",
                                              health_lost=health_lost,
                                              health_curr=self.health)
            return returned_string.format(defeated_char_name=defeated_char_name,
                                          weapon=self.equipped['Weapon'].name,
                                          health_lost=health_lost,
                                          health_curr=self.health)

    def move(self, direction: str):
        """
        Parameter
        ---------
        direction : str
            movement direction string

        Description
        -----------
        Checks if direction key exists in linked_rooms dictionary of current room
            Value of direction key is assigned to current location
        "No way" string is returned otherwise
        """
        if direction in self.location.linked_rooms:
            self.location = self.location.linked_rooms[direction]
            return f"You have moved {direction}"
        else:
            return "No way"

    def take(self):
        """
        Description
        -----------
        Checks if an item in current location exists
            Puts item in backpack
            Assigns None value to item attribute of current location
            Returns "You took item_name. And put it in your backpack." string
        Returns "There is nothing to take." string
        """
        if self.location.item:
            self.backpack[self.location.item.name] = self.location.item
            item_name = self.location.item.name
            self.location.item = None
            return f"You took {item_name}. And put it in your backpack."
        else:
            return "There is nothing to take."

    def check_backpack(self):
        """
        Description
        -----------
        Builds string of all item names, descriptions and usages of items in backpack dictionary
        Returns built string
        Returns "You have nothing in your backpack." string if backpack is empty
        """
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
        """
        Description
        -----------
         Builds string of all item names, descriptions and usages in equipped dictionary
         Returns built string
        """
        equipped_str = ""
        for body_part, item in self.equipped.items():
            if item is None:
                equipped_str += f"On {body_part} slot you have equipped nothing"
            else:
                equipped_str += f"On {body_part} slot you have equipped {item}"
        return equipped_str

    def equip(self):
        """
        Description
        -----------
        Asks user to input item name to equip
        Checks if item name exists in backpack dictionary
        Returns "You don't have this" string otherwise
        Checks if item type is equippable
            Puts item in equipped dictionary
            If item type is "Weapon" changes strength attribute of player to weapons strength attribute
            Returns "You have equipped item_name on item_type item slot" string
        Returns "You can not equip this" string otherwise
        """
        item_name = input("What item do you want to equip?\n>")
        if item_name in self.backpack:
            item = self.backpack[item_name]
        else:
            return "You don't have this"
        if item.type in self.equipped:
            self.equipped[item.type] = item
            if item.type == "Weapon":
                self.strength = item.strength
            return f"You have equipped {item.name} on {item.type} item slot"
        else:
            return "You can not equip this"

    def give(self):
        """
        Description
        -----------
        Asks user to input item name to be given.
        Checks if character exists in the current location,
        Returns "There is no one here" string if no character exists.
        Checks if item name exists in backpack dictionary,
        Returns "You don't have this" string if item is not found.
        Checks return value of give() method from character in current location,
        If True, checks class of character object
            If Friend
                Puts possession attribute value to backpack
                Sets treat and possession attribute values of character in current location to None
                Deletes item given from backpack dictionary
                Returns "character_name accepted your gift, and gave you item_name" string
            If Enemy
                Sets character attribute value of current location to None
                Deletes item given from backpack dictionary
                Returns "You fend off character_name with item_name" string
        If False
            Returns "character_name does not like item_name" string
        """
        if self.location.character:
            item = input(f"What do you want to give to {self.location.character.name}?\n>")
            if item in self.backpack:
                if self.location.character.give(item):
                    if isinstance(self.location.character, Friend):
                        loot = self.location.character.possession
                        self.backpack[loot.name] = loot
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

    def use(self):
        #TODO consume food for now, other possibilities to be discovered
        pass