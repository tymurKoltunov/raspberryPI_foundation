from room import *
from character import *


def createRooms():
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


def createChars(rooms):
    dave = Dave()
    elsa = Elsa()
    rooms['dining_hall'].character = dave
    rooms['ballroom'].character = elsa
    return rooms


