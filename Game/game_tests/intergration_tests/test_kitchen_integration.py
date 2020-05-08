from Game.bin import *

def test_cheese_can_be_taken_only_once(kitchen):
    player = Player(kitchen)
    assert player.location.item.name == "Cheese", f"location item name is not 'Cheese' it is {player.location.item.name}"
    player.take()
    assert isinstance(player.location.item, type(None)), "after 'take' action item value in location is not None"
