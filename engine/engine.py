""" created 05/09/2016
author: marcello
version: 0.1
"""
from space.galaxies import Galaxy


class Engine():
    """Game engine."""

    def __init__(self, galaxy: Galaxy, players: list):

        self._galaxy = galaxy
        self._players = players

    def play_turn(self):
        """Processes the turn."""

        pass