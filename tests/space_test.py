import unittest

from space.geometry import Coordinates2D
from space.space_objects import Planet, Star, System, Galaxy


class SpaceTest(unittest.TestCase):

    def setUp(self):

        self.co1 = Coordinates2D(0+0j)
        self.co2 = Coordinates2D(100, 100)
        self.co3 = Coordinates2D(x=200, y=200)
        self.co4 = Coordinates2D(320, 200)

        self.st1 = Star(cls='G')
        self.st2 = Star(name='star-2', cls='G')
        self.st3 = Star(name='star-3', cls='G')

        self.p1 = Planet()
        self.p2 = Planet('planet-2')
        self.p3 = Planet('planet-3')

        self.sy1 = System(star=self.st1, planets=[self.p1,], coord=(0, 0))
        self.sy2 = System(star=self.st2, planets=[self.p2, self.p3],
                          coord=(100, 100))
        self.sy3 = System(star=self.st3, planets=[], coord=(200, 200))

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

    def test_coordinates(self):

        # Coordinates2D
        self.assertTupleEqual(self.co1.coord, (0, 0))
        self.assertTupleEqual(self.co2.coord, (100, 100))
        self.assertTupleEqual(self.co3.coord, (200, 200))

        self.assertEqual(self.co1.x, 0)
        self.assertEqual(self.co2.y, 100)

        self.co4.x = 640
        self.co4.y = 400
        self.assertEqual(self.co4.coord, (640, 400))

        # System(Coordinates2D)
        self.assertEqual(self.sy1.coord, (0, 0))
        self.assertEqual(self.sy2.x, 100)
        self.assertEqual(self.sy3.y, 200)







if __name__ == '__main__':
    unittest.main()
