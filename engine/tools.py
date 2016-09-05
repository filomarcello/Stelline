""" created 05/09/2016
author: marcello
version: 0.1

Libraries with tools for objects creation
"""
from random import randint

from engine.constants import MIN_PLANETS, MAX_PLANETS, MAX_SYSTEMS, MIN_SYSTEMS
from space.space_objects import Planet, Star, System, Galaxy


def random_name():
    return 'random' # TODO: make true random names

def random_cls():
    """Randomize star class."""
    return 'G' # TODO: make true random class for stars

def random_planet():
    return Planet(name=random_name())

def random_star():
    return Star(name=random_name(), cls=random_cls())

def random_system(min_planets: int = MIN_PLANETS,
                  max_planets: int = MAX_PLANETS):
    planets = []
    for j in range(randint(min_planets, max_planets)):
        planets.append(random_planet())
    return System(name=random_name(), planets=planets, coord=(0, 0),
                  star=random_star())

def random_galaxy(min_systems: int = MIN_SYSTEMS,
                  max_systems: int = MAX_SYSTEMS):
    systems = []
    for j in range(randint(min_systems, max_systems)):
        systems.append(random_system())
    return Galaxy(systems=systems)

