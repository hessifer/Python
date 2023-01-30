import unittest

from GeometryClass import Polygon, Triangle, Rectangle, Square


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        with self.assertRaises(NotImplementedError):
            Polygon().get_sides()
        with self.assertRaises(NotImplementedError):
            Polygon().get_area()
        with self.assertRaises(NotImplementedError):
            Polygon().get_perimeter()


if __name__ == "__main__":
    unittest.main()
