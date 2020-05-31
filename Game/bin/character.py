from .item import *
from .data import *
from random import choices


class Character:
    """
    Character class represents all NPCs in the game

    Attributes
    ----------
    name : str
        name of the NPC
    description : str
        description of the NPC
    conversation : str
        what the NPC will say when talked to
        (default is empty string)
    treat : str
        special item that player can give to NPC(fends off enemies, exchanges for another item with friend)
        (default is empty string)

    Methods
    -------
    describe()
        returns formatted string "{self.name} is here! \n{self.description}"
    talk()
        if self.conversation attribute is not empty returns formatted string "[{self.name} says]: {self.conversation}"
        otherwise returns formatted string "({self.name} doesn't want to talk to you"
    fight(strength = 0)
        returns formatted string "{self.name} doesn't want to fight with you"
    give(item)
        returns True if passed string matches self.treat attribute
        returns False otherwise
    """

    # Create a character
    def __init__(self, name: str, description: str, conversation='', treat=''):
        self.name = name
        self.description = description
        self.conversation = conversation
        self.treat = treat

    @property
    def treat(self):
        return self._treat

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def conversation(self):
        return self._conversation

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    @conversation.setter
    def conversation(self, conv):
        self._conversation = conv

    @treat.setter
    def treat(self, treat):
        self._treat = treat

    # Describe this character
    def describe(self):
        return f"{self.name} is here! \n{self.description}"

    # Talk to this character
    def talk(self):
        if self._conversation:
            return f"[{self.name} says]: {self.conversation}"
        else:
            return f"({self.name} doesn't want to talk to you"

    # Fight with this character
    def fight(self, strength=0):
        return f"{self.name} doesn't want to fight with you"

    def give(self, item: str):
        if item in self.treat:
            return True
        else:
            return False


class Enemy(Character):

    def __init__(self, name: str, description: str, strength: int, treat='', conversation='', loot=Item):
        super().__init__(name, description, conversation, treat)
        self.strength = strength
        self.loot = loot

    @property
    def loot(self):
        return self._loot

    @loot.setter
    def loot(self, loot):
        self._loot = loot

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    def fight(self, strength=0):
        health_lost = 0
        result = [True, False]
        difference = (strength - self.strength) * 5
        win_chance = base_win_chance + difference
        chances = [win_chance, 100 - win_chance]
        fight_sequence = choices(result, chances, k=10)
        for success in fight_sequence:
            if not success:
                health_lost += one_hit_damage
                if health_lost == 5:
                    return health_lost
            else:
                return health_lost


class Friend(Character):

    def __init__(self, name: str, description: str, conversation='', treat='', possession=Item):
        super().__init__(name, description, conversation, treat)
        self.possession = possession

    @property
    def possession(self):
        return self._possession

    @possession.setter
    def possession(self, pos):
        self._possession = pos
