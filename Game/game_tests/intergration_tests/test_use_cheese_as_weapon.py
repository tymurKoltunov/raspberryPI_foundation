from Game.bin.room import *
from Game.bin.character import *
from Game.bin.setup import *
from Game.bin.player import *

def test_use_cheese_as_weapon():
    rooms = create_rooms()
    player = Player(rooms['dining_hall'])
    player.backpack["Cheese"] = Cheese()
    assert "fend" in player.fight(player.backpack["Cheese"])