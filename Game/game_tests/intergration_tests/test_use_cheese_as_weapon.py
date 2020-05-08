from Game.bin import *

def test_cheese_as_weapon_on_dave():
    rooms = create_rooms()
    player = Player(rooms['dining_hall'])
    player.backpack["Cheese"] = Cheese()
    assert "fend" in player.fight(player.backpack["Cheese"])


