class Room:
    def __init__(self, name="", description=""):
        self._name = name
        self._description = description
        self.linked_rooms = {}
        self._character = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def character(self):
        return self._character

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    @character.setter
    def character(self, char):
        self._character = char

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("The " + self.name + "\n" + "-" * 20)
        for direction in self.linked_rooms:
            print("The " + self.linked_rooms[direction].name + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("No way")
            return self