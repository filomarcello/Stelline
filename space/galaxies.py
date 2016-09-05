""" created 05/09/2016
author: marcello
version: 0.1
"""

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
