class SuperPower():

    name = None

    def __init__(self, name):
        self.name = name

    def use(self):
        print('Super Power Used')


class SuperHero:

    first_name = None
    second_name = None

    def __init__(self, first_name, second_name, super_power):
        self.first_name = first_name
        self.second_name = second_name
        self.super_power = super_power

    def get_first_name(self):
        return self.first_name

    def get_second_name(self):
        return self.second_name

    def get_full_name(self):
        return self.first_name + ' ' + self.second_name

    def attack(self):
        self.super_power.use()

