from .room import *


def create_rooms():
    kitchen = Kitchen()
    dining_hall = DiningHall()
    ballroom = Ballroom()
    dave = Enemy(dave_name,
                 dave_description,
                 dave_conversation,
                 dave_weakness)
    elsa = Friend(elsa_name,
                  elsa_description,
                  elsa_conversation,
                  elsa_possession,
                  elsa_treat)
    cheese = Food(cheese_name,
                  cheese_description,
                  cheese_charges,
                  cheese_usage)
    kitchen.item = cheese
    dining_hall.character = dave
    ballroom.character = elsa
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    return kitchen




