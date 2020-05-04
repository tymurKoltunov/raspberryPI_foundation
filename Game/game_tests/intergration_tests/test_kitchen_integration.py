import Game.bin.player
import Game.bin.room
import Game.bin.item
from Game.game_tests.unit_tests.test_kitchen_unit import *
from Game.bin.player import *


def test_cheese_can_be_taken_only_once(kitchen):
    player = Player(kitchen)
    assert player.location.item.name == "Cheese"
    player.take()
    assert isinstance(player.location.item, type(None))
