from room import *
from character import *
from setup import *
from player import *

rooms = create_rooms()
player = Player(rooms['kitchen'])

def fight():
    weapon = input("What will you use as a weapon?")
    if weapon in player.backpack:
        player.fight(weapon)
    else:
        print("You don't have this.")

def indirect(command):
    switcher = {
        'south': player.move('south'),
        'north': player.move('north'),
        'west': player.move('west'),
        'east': player.move('east'),
        'inspect': player.location.inspect(),
        'talk': player.talk(),
        'fight': fight,
    }
    func = switcher.get(command, 'Invalid')
    return func()

while True:
    print("\n")
    player.location.get_details()
    if player.location.character is not None:
        player.location.character.describe()
    command = input("> ")
    indirect(command)

