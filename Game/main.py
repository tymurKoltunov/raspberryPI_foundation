from room import Room
from character import Enemy, Friend

kitchen = Room('Kitchen')
kitchen.description = "A dank and dirty room buzzing with flies."
dining_hall = Room('Dining Hall')
dining_hall.description = "About twice as big as kitchen, with big table in the middle and some scattered chairs. looks completely abandoned."
ballroom = Room("Ballroom")
ballroom.description = "Big room with an even bigger window, which hasn't been washed for a long time, fill room  with grey light."
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"
dining_hall.character = dave

elsa = Friend("Elsa", "Little girl")
elsa.conversation = "What are you doing here?"
ballroom.character = elsa

current_room = kitchen
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
