import unittest

from space.galaxies import Galaxy
from space.star_systems import Planet, Star, System


class SpaceTest(unittest.TestCase):

    def setUp(self):

        self.st1 = Star(cls='G')
        self.st2 = Star(name='star-2', cls='G')
        self.st3 = Star(name='star-3', cls='G')

        self.p1 = Planet()
        self.p2 = Planet('planet-2')
        self.p3 = Planet('planet-3')

        self.sy1 = System(star=self.st1, planets=[self.p1,])
        self.sy2 = System(star=self.st2, planets=[self.p2, self.p3])
        self.sy3 = System(star=self.st3, planets=[])

        self.g1 = Galaxy(systems=[self.sy1, self.sy2, self.sy3])


    def test_iteration(self):

         for p in self.sy1:
             self.assertEqual(p, self.p1)

         for p in self.sy2:
             self.assertIn(p, [self.p2, self.p3])

         for p in self.sy3:
             self.assertIsNone(p)

         for s in self.g1:
             self.assertIn(s, [self.sy1, self.sy2, self.sy3])



if __name__ == '__main__':
    unittest.main()
