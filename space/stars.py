""" created 12/01/2016
author: marcello
"""
from space.tools import star_random_class


class Star:

    def __init__(self, name: str = 'star', cls: str = None, label: str = None):
        """If cls (spectral class) left None, it will be random."""

        self.name = name
        self.label = label
        if cls:
            self.cls = cls
        else:
            self.cls = star_random_class()

        # TODO: other physical parameters: mass, temperature, etc.

class Planet:

    def __init__(self, name: str = 'planet', ):

        pass