from .item import *
from .data import *
from random import choices


class Character:
    """
    Description
    -----------
    Super class for all NPCs in the game
    Sub classes are Friend, Enemy\n

    Instance variables
    -----------------

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

    Instance Methods
    ---------------
    describe()
        describes NPC
    talk()
        talks to the NPC
    fight(strength: int)
        fights with NPC
        (player can only fight enemies)
    give(item)
        gives item to an NPc

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
        """
        Description
        -----------
        returns formatted string "{self.name} is here! {self.description}"
        """
        return f"{self.name} is here! \n{self.description}"

    # Talk to this character
    def talk(self):
        """
        Description
        -----------
        if self.conversation attribute is not empty returns formatted string "[{self.name} says]: {self.conversation}"\n
        otherwise returns formatted string "({self.name} doesn't want to talk to you"
        """
        if self._conversation:
            return f"[{self.name} says]: {self.conversation}"
        else:
            return f"({self.name} doesn't want to talk to you"

    # Fight with this character
    def fight(self, strength: int):
        """
        Parameter
        ---------
        strength : int
            strength of the player

        Description
        ----------
        returns formatted string "{self.name} doesn't want to fight with you"\n
        it is overridden in enemy class
        """
        return f"{self.name} doesn't want to fight with you"

    def give(self, item: str):
        """
        Parameter
        ---------
        item : str
            name of the item player wants to give to NPC

        Description
        -----------
        returns True if passed string matches self.treat attribute\n
        returns False otherwise
        """
        if item in self.treat:
            return True
        else:
            return False


class Enemy(Character):
    """
    Description
    -----------
    Represents hostile NPCs in the game with which player can fight
    Subclass of Character class\n

    Instance variables
    -----------------

    name : str
        name of the NPC
    description : str
        description of the NPC
    strength : int
        strength of the NPC, number
    loot : Item
        item which will be looted by player, if player defeats this NPC in a fight
    conversation : str
        what the NPC will say when talked to
        (default is empty string)
    treat : str
        special item that player can give to NPC(fends off enemies, exchanges for another item with friend)
        (default is empty string)

    Instance methods
    -----------------

    fight(strength: int)
        fights with NPC
    """
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

    def fight(self, strength: int):
        """
        Parameter
        ---------
        strength : int
            strength of the player who fights a monster

        Description
        -----------
        returns amount of lost health by the player\n
        fight system described in /docs/fight_system.txt
        """
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
    """
    Description
    -----------
    Represents friendly NPCs with which player can not fight
    Subclass of Character class

    Instance variables
    -----------------
    name : str
        name of the NPC
    description : str
        description of the NPC
    possession: Item
        given to player if player gives treat to a NPC
    conversation : str
        what the NPC will say when talked to
        (default is empty string)
    treat : str
        special item that player can give to NPC(fends off enemies, exchanges for another item with friend)
        (default is empty string)
    """
    def __init__(self, name: str, description: str, conversation='', treat='', possession=Item):
        super().__init__(name, description, conversation, treat)
        self.possession = possession

    @property
    def possession(self):
        return self._possession

    @possession.setter
    def possession(self, pos):
        self._possession = pos
