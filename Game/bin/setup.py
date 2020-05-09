from .room import *


def create_rooms():
    kitchen = Kitchen()
    dining_hall = DiningHall()
    ballroom = Ballroom()
    dave = Enemy(dave_name,
                 dave_description,
                 dave_conversation,
                 globals()[dave_weakness]())
    elsa = Friend(elsa_name,
                  elsa_description,
                  elsa_conversation,
                  globals()[elsa_possession](),
                  globals()[elsa_treat]())
    dining_hall.character = dave
    ballroom.character = elsa
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    return kitchen




