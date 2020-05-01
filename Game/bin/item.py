class Item:
    def __init__(self, name="", description="", type=""):
        self.name = name
        self.description = description
        self.type = type
        self.stats = {}

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    def get_details(self):
        print(self.description)
        for k, v in self.stats.items():
            print(k, v)

class Cheese(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Cheese'
        self.description = 'Big and smelly piece of cheese'
        self.type = 'Food'
        self.stats['usage'] = 'Can be used as weapon'


class Tiara(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Tiara'
        self.description = 'Silver tiara with glowing gemstome in the center of it'
        self.type = 'Accessory'
        self.stats['usage'] = 'Grants night vision'


class Candy(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Candy'
        self.type = 'Food'
        self.stats['usage'] = 'Liked by kids'
