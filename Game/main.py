from room import Room

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

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)