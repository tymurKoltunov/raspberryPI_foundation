from Game.bin import *
import inspect


def indirect(command):
    switcher = {
        'south': player.move,
        'north': player.move,
        'west': player.move,
        'east': player.move,
        'inspect': player.location.inspect,
        'talk': player.talk,
        'fight': player.fight,
        'take': player.take,
        'backpack': player.check_backpack,
        'equip': player.equip,
        'equipped': player.check_equipped,
        'exit': lambda: ending
    }
    func = switcher.get(command, lambda: 'Invalid')
    return func


room = create_rooms()
player = Player(room)

print(intro)
while True:

    player.location.get_details()
    if player.location.character is not None:
        print(f"\n{player.location.character.describe()}")
    if player.location.exit:
        print("\nIt seems there is an exit here. Type 'exit' to finish the game.")
    command = input("> ")
    action = indirect(command)
    if inspect.getfullargspec(action).args.__len__() > 1:
        print(action(command))
    else:
        result_of_action = action()
        print(result_of_action)
        if "crushes you, puny adventurer" in result_of_action:
            break
        if ending in result_of_action:
            break

