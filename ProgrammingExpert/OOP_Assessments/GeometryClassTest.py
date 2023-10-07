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

    def test_case_2(self):
        triangle = Triangle(1, 1, 1)
        self.assertEqual(3, triangle.get_perimeter())
        rect = Rectangle(2, 3)
        self.assertEqual(10, rect.get_perimeter())
        square = Square(3)
        self.assertEqual(12, square.get_perimeter())

    def test_case_3(self):
        triangle = Triangle(1, 5, 6)
        self.assertEqual([1, 5, 6], sorted(triangle.get_sides()))
        rect = Rectangle(2, 3)
        self.assertEqual([2, 2, 3, 3], sorted(rect.get_sides()))
        square = Square(3)
        self.assertEqual([3, 3, 3, 3], sorted(square.get_sides()))

    def test_case_4(self):
        triangle = Triangle(2, 5, 6)
        self.assertAlmostEqual(4.68, triangle.get_area(), delta=0.01)
        rect = Rectangle(2, 3)
        self.assertEqual(6, rect.get_area())
        square = Square(5)
        self.assertEqual(25, square.get_area())

if __name__ == "__main__":
    unittest.main()
