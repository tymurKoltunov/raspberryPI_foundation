def move(): return 'player moves'

def inspect(): return 'player inspects the room he currently in'

def talk(): return 'player talks to the character who is in same room as the player '

def fight(): return 'player fights character who is in the same room as player'

def indirect(command):
    switcher = {
        'south': move,
        'north': move,
        'west': move,
        'east' : move,
        'inspect': inspect,
        'talk': talk,
        'fight': fight,
    }
    func = switcher.get(command, lambda: 'Invalid')
    return func()

indirect('talk')
