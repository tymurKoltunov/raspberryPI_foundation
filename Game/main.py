from room import *
from character import *
from setup import *

rooms = createRooms()
rooms = createChars(rooms)

current_room = rooms['kitchen']
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        current_room.character.talk()
    elif command == "inspect":
        current_room.inspect()
    elif command == "fight":
        print("What will you use as a weapon?")
        if not current_room.character.fight(input("I choose: ")):
            break
