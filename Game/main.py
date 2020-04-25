from room import Room
from character import Enemy, Friend
from setup import createRooms

rooms = createRooms()

dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"
dining_hall.character = dave

elsa = Friend("Elsa", "Little girl")
elsa.conversation = "What are you doing here?"
ballroom.character = elsa
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
    elif command == "fight":
        print("What will you use as a weapon?")
        if not current_room.character.fight(input("I choose: ")):
            break
