class Item:
    def __init__(self, name="", description="", type=""):
        self._name = name
        self._description = description
        self._type = type
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
