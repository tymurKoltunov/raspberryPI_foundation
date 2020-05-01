from room import *
from character import *
from setup import *
from player import *
import inspect

rooms = create_rooms()
player = Player(rooms['kitchen'])

def fight():
    weapon = input("What will you use as a weapon? \n")
    if weapon in player.backpack:
        player.fight(weapon)
    else:
        print("You don't have this.")

def indirect(command):
    switcher = {
        'south': player.move,
        'north': player.move,
        'west': player.move,
        'east': player.move,
        'inspect': player.location.inspect,
        'talk': player.talk,
        'fight': fight,
        'take': player.take,
        'backpack': player.check_backpack
    }
    func = switcher.get(command, lambda: print('Invalid'))
    return func

while True:
    print("\n")
    player.location.get_details()
    if player.location.character is not None:
        player.location.character.describe()
    command = input("> ")
    action = indirect(command)
    if inspect.getfullargspec(action).args.__len__() > 1:
        action(command)
    else:
        action()


