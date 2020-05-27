from .item import *
from .data import *
from random import choices


class Character:

    # Create a character
    def __init__(self, name: str, description: str, conversation: str, treat: str):
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
        return f"{self._name} is here! \n{self._description}"

    # Talk to this character
    def talk(self):
        if self._conversation:
            return f"[{self._name} says]: {self._conversation}"
        else:
            return f"({self._name} doesn't want to talk to you"

    # Fight with this character
    def fight(self, strength=0):
        return f"{self._name} doesn't want to fight with you"

    def give(self, item):
        if item in self.treat:
            return True
        else:
            return False


class Enemy(Character):

    def __init__(self, name: str, description: str, conversation: str, treat: str, strength: int):
        super().__init__(name, description, conversation, treat)
        self.strength = strength

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
        chances = [win_chance, 100-win_chance]
        fight_sequence = choices(result, chances, k=10)
        for success in fight_sequence:
            if not success:
                health_lost += one_hit_damage
                if health_lost == 5:
                    return health_lost
            else:
                return health_lost


class Friend(Character):

    def __init__(self, name: str, description: str, conversation: str, treat: str, possession=Item):
        super().__init__(name, description, conversation, treat)
        self.possession = possession

    @property
    def possession(self):
        return self._possession

    @possession.setter
    def possession(self, pos):
        self._possession = pos
