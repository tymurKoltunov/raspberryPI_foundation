from .room import *


def create_rooms():
    rooms = {}
    kitchen = Kitchen()
    dining_hall = DiningHall()
    ballroom = Ballroom()
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    rooms['kitchen'] = kitchen
    rooms['dining_hall'] = dining_hall
    rooms['ballroom'] = ballroom
    return rooms



