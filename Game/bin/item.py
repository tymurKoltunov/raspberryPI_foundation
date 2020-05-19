class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.type = None
        self.usage = None

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
    def __init__(self, name, description, charges, usage):
        super().__init__(name, description)
        self.type = 'Food'
        self.charges = charges
        self.usage = usage

    @property
    def charges(self):
        return self._charges

    @charges.setter
    def charges(self, charges):
        self._charges = charges


class Accessory(Item):
    def __init__(self, name, description, usage):
        super().__init__(name, description)
        self.type = 'Accessory'
        self.usage = usage


class Weapon(Item):
    def __init__(self, name, description, strength):
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
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Head'


class Torso(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Torso'


class Hands(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Hands'


class Legs(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Legs'


class Feet(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Feet'
