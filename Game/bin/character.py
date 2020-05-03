from .item import *


class Character:

    # Create a character
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description
        self.conversation = None

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

    # Describe this character
    def describe(self):
        return f"{self._name} is here! \n{self._description}"

    # Talk to this character
    def talk(self):
        if self._conversation:
            return f"[ {self._name} says]: {self._conversation}"
        else:
            return f"({self._name} doesn't want to talk to you"

    # Fight with this character
    def fight(self, weapon):
        return f"{self._name} doesn't want to fight with you"


class Enemy(Character):

    def __init__(self):
        super().__init__()
        self._weakness = None

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, weakness):
        self._weakness = weakness

    def fight(self, weapon):
        if weapon.name == self.weakness.name:
            return f"You fend {self.name} off with the  + {weapon}"
        else:
            return f"{self.name} crushes you, puny adventurer"


class Friend(Character):

    def __init__(self):
        super().__init__()
        self._treat = None
        self._possession = None

    @property
    def treat(self):
        return self._treat

    @property
    def possession(self):
        return self._possession

    @treat.setter
    def treat(self, treat):
        self._treat = treat

    @possession.setter
    def possession(self, pos):
        self._possession = pos

class Dave(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Dave"
        self.description = "A smelly zombie"
        self.weakness = Cheese()
        self.conversation = 'BRRRRRAAAAINS'

class Elsa(Friend):
    def __init__(self):
        super().__init__()
        self.name = "Elsa"
        self.description = "Little girl"
        self.possession = Tiara()
        self.treat = Candy()
        self.conversation = "What are you doing here?"