from unittest.mock import sentinel

from src.dummy import SuperHero


def test_super_hero():
    hero = SuperHero(first_name='Doctor', second_name='Strange', super_power=sentinel)
    print(hero.get_full_name())