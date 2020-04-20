class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(self.description)

    @property
    def name(self):
        return self._name

    def description(self):
        return self._description

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc
