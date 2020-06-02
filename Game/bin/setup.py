from .room import *


def create_rooms(room_name=spawn_room):
    """
    Parameter
    ---------
    room_name: str
        room name to be returned
        (default is spawn_room which is defined in data.py)

    Description
    -----------
    creates rooms, items, characters everything which constitutes game world\n
    returns room object, name attribute of which matches room_name parameter\n
    if passed parameter does not match any rooms that were created, then default is returned
    """
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
                  locals()[elsa_possession.lower()])
    kitchen = Room(kitchen_name,
                   kitchen_description,
                   kitchen_inspect,
                   locals()[kitchen_item.lower()])
    dining_hall = Room(name=dining_hall_name,
                       description=dining_hall_description,
                       inspect=dining_hall_inspect,
                       character=locals()[dining_hall_character.lower()])
    ballroom = Room(ballroom_name,
                    ballroom_description,
                    ballroom_inspect,
                    locals()[dining_hall_item.lower()],
                    locals()[ballroom_character.lower()])
    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    ballroom.exit = True
    return locals()[room_name] if locals()[room_name] else locals()[spawn_room.lower()]
