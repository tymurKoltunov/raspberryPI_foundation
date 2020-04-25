class Character:

    # Create a character
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def conversation(self):
        return self._conversation

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    @conversation.setter
    def conversation(self, conv):
        self._conversation = conv

    # Describe this character
    def describe(self):
        print(self._name + " is here!")
        print(self._description)

    # Talk to this character
    def talk(self):
        if self._conversation is not None:
            print("[" + self._name + " says]: " + self._conversation)
        else:
            print(self._name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item=""):
        print(self._name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._weakness = None

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, weakness):
        self._weakness = weakness

    def fight(self, combat_item=""):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


class Friend(Character):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._treat = None
        self._possession = None

    @property
    def treat(self):
        return self._treat

    @property
    def possession(self):
        return self._possession

    @treat.setter
    def treat(self, treat):
        self._treat = treat

    @possession.setter
    def possession(self, pos):
        self._possession = pos