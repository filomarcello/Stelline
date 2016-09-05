""" created 12/01/2016
author: marcello
"""
from space.geometry import Coordinates2D
from space.tools import star_random_class


class Star():

    def __init__(self, cls: str, name: str = 'star'):
        """If cls (spectral class) left None, it will be random."""

        self._name = name
        self._cls = cls

        # TODO: other physical parameters: mass, temperature, etc.


class Planet():
    """Implements a planet with mineral and physics featuire."""

    def __init__(self, name: str = 'planet'):

        self._name = name

        # TODO: other physical parameters: mass, temperature, etc.

class Asteroids(Planet):
    """Implements a belt of asteroids."""

    def __init__(self, density: float, name: str = 'asteroids'):

        super().__init__(name)
        self._density = density

    pass # TODO: other physical parameters


class System(Coordinates2D):
    """One star with 0 or + planet(s).

    Can iterate on planets.""" # TODO: multiple stars system

    def __init__(self, star: Star,
                 planets: list,
                 coord = (0, 0),
                 name: str = 'system'):
        """Accepts two list: stars and planet. Coord is (x, y)."""

        super().__init__(coord[0], coord[1])
        self._name = name
        self._star = star
        self._planets = planets

    # iteration protocol

    def __iter__(self):
        self._curr = 0
        return self

    def __next__(self):
        self._curr += 1
        if self._curr > len(self._planets):
            raise StopIteration
        else:
            return self._planets[self._curr - 1]


class Galaxy():
    """A collection of solar systems.

    Allows iterating on its systems."""

    def __init__(self, systems: list):

        self._systems = systems
        self._n_systems = len(self._systems)

    # iteration protocol

    def __iter__(self):
        self._curr = 0
        return self

    def __next__(self):
        self._curr += 1
        if self._curr > self._n_systems:
            raise StopIteration
        else:
            return self._systems[self._curr - 1]




