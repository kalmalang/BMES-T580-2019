import random

class Creature(object):

    def __init__(self, name, level):

        self.name = name
        self.level = level

    def print(self):

        print('Name: ', self.name, 'Level: ', self.level)

    def attack_roll(self):
        die = random.randint(1,20)
        return die*self.level

    def defense_roll(self):
        die = random.randint(1,20)
        return die*self.level

class Event(object):

    def __init__(self, type, strength):

        self.type = type
        self.strength = strength

class Wizard(Creature):

    def __init__(self, name, level, typ=None):

        self.name = name
        self.level = level
        self.typ = typ

    def level_up(self):
        self.level += 1

    def level_down(self):
        self.level -= 1

    def print(self):

        print('Name: ', self.name, 'Level: ', self.level, 'Type: ', self.typ)

class IceWizard(Wizard):

    def __init__(self, name, level, typ='Ice'):

        self.name = name
        self.level = level
        self.typ = typ


if __name__ == '__main__':







    joe = Wizard('Wiz', 9)
    ana = IceWizard('IceWiz', 10)

    octopus = Creature('Cephalopod', 8)
    hummingbird = Creature('Colibri', 5)

    octopus.print()
    hummingbird.print()
    joe.print()
    ana.print()

    print(octopus.defense_roll(), hummingbird.attack_roll(), joe.attack_roll())