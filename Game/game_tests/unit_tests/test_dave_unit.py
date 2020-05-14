from Game.bin import *

def test_name_should_be_dave(dining_hall):
    assert dining_hall.character.name is dave_name, \
        f"got: {dining_hall.character.name} \nexpected {dave_name}"

def test_description_match(dining_hall):
    assert dining_hall.character.description is dave_description, \
        f"got: {dining_hall.character.description}\nexpected: {dave_description}"

def test_conversation_should_match(dining_hall):
    assert dining_hall.character.conversation is dave_conversation, \
        f"got: {dining_hall.character.conversation} \nexpected: {dave_conversation}"

def test_weakness_should_be_cheese(dining_hall):
    assert dining_hall.character.weakness.name is dave_weakness, \
        f"got: {dining_hall.character.weakness.name} , expected: {dave_weakness}"

