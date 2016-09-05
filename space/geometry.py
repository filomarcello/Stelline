""" created 05/09/2016
author: marcello
version: 0.1
"""
from functools import singledispatch


class Coordinates2D():
    """Base class for objects located in a 2D space.

    To be extended by classes that needs to have (x, y) coordinates.
    Wraps a complex number c where x is Re(c)
    """

    def __init__(self, *args, **kwargs):
        """Accepts a 2-elements list (x, y), a complex, or x an y arguments."""

        if args and isinstance(args[0], complex):
            x = args[0].real
            y = args[0].imag
            self._coord = complex(x, y)
            return
        elif len(args) == 2:
            x = args[0]
            y = args[1]
            self._coord = complex(x, y)
            return
        else:
            x = kwargs['x']
            y = kwargs['y']
            self._coord = complex(x, y)


    # properties and operators

    @property
    def x(self):
        return self._coord.real

    @x.setter
    def x(self, value):
        self._coord = complex(value, self._coord.imag)

    @property
    def y(self):
        return self._coord.imag

    @y.setter
    def y(self, value):
        self._coord = complex(self._coord.real, value)

    @property
    def coord(self):
        return self._coord.real, self._coord.imag

    @coord.setter
    def coord(self, x, y):
        self._coord = complex(x, y)


class Velocity():
    pass


