from .room import *


def create_rooms(room_name = 'kitchen'):
    kitchen = Kitchen()
    dining_hall = DiningHall()
    ballroom = Ballroom()
    cheese = Food(cheese_name,
                  cheese_description,
                  cheese_charges,
                  cheese_usage)
    candy = Food(candy_name,
                 candy_description,
                 candy_charges,
                 candy_usage)
    tiara = Accessory(tiara_name,
                      tiara_description,
                      tiara_usage)
    dave = Enemy(dave_name,
                 dave_description,
                 dave_conversation,
                 dave_treat)
    elsa = Friend(elsa_name,
                  elsa_description,
                  elsa_conversation,
                  elsa_treat,
                  locals()[elsa_possession.lower()] )
    kitchen.item = locals()[kitchen_item.lower()]
    dining_hall.character = locals()[dining_hall_character.lower()]
    ballroom.character = locals()[ballroom_character.lower()]
    dining_hall.item = locals()[dining_hall_item.lower()]
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    ballroom.exit = True
    return locals()[room_name]




