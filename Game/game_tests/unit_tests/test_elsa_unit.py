from Game.bin import *

def test_name_should_be_elsa(ballroom):
    assert ballroom.character.name is elsa_name, \
        f"got: {ballroom.character.name} \nexpected {elsa_name}"

def test_description_match(ballroom):
    assert ballroom.character.description is elsa_description, \
        f"got: {ballroom.character.description}\nexpected: {elsa_description}"

def test_conversation_should_match(ballroom):
    assert ballroom.character.conversation is elsa_conversation, \
        f"got: {ballroom.character.conversation} \nexpected: {elsa_conversation}"

def test_possession_should_be_tiara(ballroom):
    assert ballroom.character.possession.name is elsa_possession, \
        f"got: {ballroom.character.possession.name} , expected: {elsa_possession}"

def test_treat_should_be_candy(ballroom):
    assert ballroom.character.treat.name is elsa_treat, \
        f"got: {ballroom.character.treat.name} , expected: {elsa_treat}"