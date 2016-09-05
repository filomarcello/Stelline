import unittest

from engine.constants import MIN_PLANETS, MAX_PLANETS, MIN_SYSTEMS, MAX_SYSTEMS
from engine.tools import random_planet, random_star, random_system, \
    random_galaxy
from space.space_objects import Planet, Star, System, Galaxy


class EngineTest(unittest.TestCase):

    def setUp(self):
        self.g1 = random_galaxy()
        self.g2 = random_galaxy(min_systems=100, max_systems=200)

    def test_random_planet(self):
        self.assertIsInstance(random_planet(), Planet)

    def test_random_star(self):
        self.assertIsInstance(random_star(), Star)

    def test_random_system(self):

        s1 = random_system()
        self.assertIsInstance(s1, System)
        self.assertGreaterEqual(len(s1._planets), MIN_PLANETS)
        self.assertLessEqual(len(s1._planets), MAX_PLANETS)
        self.assertIsInstance(s1._star, Star)

        s2 = random_system(min_planets=5, max_planets=20)
        self.assertGreaterEqual(len(s2._planets), 5)
        self.assertLessEqual(len(s2._planets), 20)

    def test_random_galaxy(self):

        self.assertIsInstance(self.g1, Galaxy)
        self.assertGreaterEqual(len(self.g1._systems), MIN_SYSTEMS)
        self.assertLessEqual(len(self.g1._systems), MAX_SYSTEMS)

        self.assertGreaterEqual(len(self.g2._systems), 100)
        self.assertLessEqual(len(self.g2._systems), 200)



if __name__ == '__main__':
    unittest.main()
