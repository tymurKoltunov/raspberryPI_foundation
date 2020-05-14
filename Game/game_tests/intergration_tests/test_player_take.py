from Game.bin import *


def test_item_can_be_taken_only_once(kitchen):
    player = Player(kitchen)
    cheese = Food(cheese_name, cheese_description, cheese_charges, cheese_usage)
    player.location.item = cheese
    player.take()
    assert isinstance(player.location.item, type(None)), "after 'take' action item value in location is not None"
