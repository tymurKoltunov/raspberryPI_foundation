class Item:
    """
    Description
    -----------
    Super class of every item that player can put in backpack
    Sub classes are Food, Accessory, Weapon, Head, Torso, Hands, Legs, Feet\n

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type
    usage : str
        description of how the item can be used
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.type = ''
        self.usage = ''

    @property
    def usage(self):
        return self._usage

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def type(self):
        return self._type

    @usage.setter
    def usage(self, usage):
        self._usage = usage

    @type.setter
    def type(self, type):
        self._type = type

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc


class Food(Item):
    """
    Description
    -----------
    Represents food items in the game

    Instance variables
    -----------------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Food')
    usage : str
        description of how the item can be used
    charges : int
        how many times food can be used
    heal_amount : int
        number of hearts restored by single use
    """
    def __init__(self, name: str, description: str, usage: str, charges: int, heal_amount : int):
        super().__init__(name, description)
        self.type = 'Food'
        self.charges = charges
        self.usage = usage
        self.heal_amount = heal_amount

    @property
    def charges(self):
        return self._charges

    @charges.setter
    def charges(self, charges):
        self._charges = charges

    @property
    def heal_amount(self):
        return self._heal_amount

    @heal_amount.setter
    def heal_amount(self, heal_amount):
        self._heal_amount = heal_amount


class Accessory(Item):
    """
    Description
    -----------
    Represents all items that can be equipped by player on Accessory item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Accessory')
    usage : str
        description of how the item can be used
    """
    def __init__(self, name: str, description: str, usage: str):
        super().__init__(name, description)
        self.type = 'Accessory'
        self.usage = usage


class Weapon(Item):
    """
    Description
    -----------
    Represents all weapons in the game\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Weapon0
    strength : str
        weapon power
    """
    def __init__(self, name: str, description: str, strength: int):
        super().__init__(name, description)
        self.type = 'Weapon'
        self.strength = strength

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength
        
        
class Head(Item):
    """
    Description
    -----------
    Represents all items that can be equipped by player on Head item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Head')
    """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.type = 'Head'


class Torso(Item):
    """
    Description
    -----------
    Represents all items that can be equipped by player on Torso item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Torso')
    """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.type = 'Torso'


class Hands(Item):
    """
    Description
    -----------
    Represents all items that can be equipped by player on Hands item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Hands')
    """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.type = 'Hands'


class Legs(Item):
    """
    Description
    -----------
    Represents all items that can be equipped by player on Legs item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Legs')
    """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.type = 'Legs'


class Feet(Item):
    """Description
    -----------
    Represents all items that can be equipped by player on Feet item slot\n
    Sub class of Item

    Instance variables
    --------
    name : str
        item name
    description : str
        item description
    type : str
        item type(is 'Feet')
        """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.type = 'Feet'
