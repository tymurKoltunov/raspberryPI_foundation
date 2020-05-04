import bin
import inspect

rooms = bin.create_rooms()
player = bin.Player(rooms['kitchen'])

def fight():
    if player.location.character is None:
        return "There is no one to fight here."
    weapon = input("What will you use as a weapon? \n")
    if weapon in player.backpack:
        return f"{player.fight(player.backpack[weapon])}"
    else:
        return "You don't have this."

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
    func = switcher.get(command, lambda: 'Invalid')
    return func


while True:
    print("\n")

    player.location.get_details()

    if player.location.character is not None:
        print( f"{player.location.character.describe()}")
    command = input("> ")
    action = indirect(command)
    if inspect.getfullargspec(action).args.__len__() > 1:
        print(action(command))
    else:
        result_of_action = action()
        print(result_of_action)
        if "crushes you, puny adventurer" in result_of_action:
            break

