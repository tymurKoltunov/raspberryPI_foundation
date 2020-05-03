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
        if self.location.character:
            return self.location.character.talk()
        else:
            return "There is no one to talk to."

    def fight(self, weapon):
        fight_result = self.location.character.fight(weapon)
        if "fend" in fight_result:
            self.location.character = None
        return fight_result

    def move(self, direction):
        if direction in self.location.linked_rooms:
            self.location = self.location.linked_rooms[direction]
            return f"You have moved {direction}."
        else:
            return "No way"

    def take(self):
        if self.location.item:
            self.backpack[self.location.item.name] = self.location.item
            item_name = self.location.item.name
            self.location.item = None
            return f"You took {item_name}. And put it in your backpack."
        else:
            return "There is nothing to take."

    def check_backpack(self):
        if self.backpack:
            for item in self.backpack:
                return self.backpack[item].name + " " + self.backpack[item].description + "\n"
        else:
            return "You have nothing in your backpack."
