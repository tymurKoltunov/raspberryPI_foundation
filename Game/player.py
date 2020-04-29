class Player:
    def __init__(self, current_pos, name='defalut'):
        self.name = name
        self.location = current_pos
        self.backpack = {}

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @location.setter
    def location(self, location):
        self._location = location

    def talk(self):
        self.location.character.talk()

    def fight(self, weapon):
        self.location.character.fight(weapon)

    def move(self, direction):
        if direction in self.location.linked_rooms:
            self.location = self.location.linked_rooms[direction]

        else:
            print("No way")

    def take(self):
        self.backpack[self.location.item.name] = self.location.item
        self.location.item = None

    def check_backpack(self):
        for item in self.backpack:
            print(self.backpack[item].name + " " + self.backpack[item].description + "\n")
