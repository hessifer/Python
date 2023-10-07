# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest
import math

from VectorClass import Vector


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(hasattr(Vector, '__repr__'))
        self.assertNotEqual(repr(Vector(1, 2)), repr(Vector(2, 1)))
        self.assertNotEqual(repr(Vector(1, 2)), repr(Vector(1, 3)))
        self.assertEqual(repr(Vector(1, 2)), repr(Vector(1, 2)))

    def test_case_2(self):
        self.assertTrue(hasattr(Vector, '__eq__'))
        self.assertNotEqual(Vector(1, 2), Vector(2, 1))
        self.assertNotEqual(Vector(1, 2), Vector(1, 3))
        self.assertEqual(Vector(1, 2), Vector(1, 2))

    def test_case_3(self):
        self.assertTrue(hasattr(Vector, '__add__'))
        v1 = Vector(4, 5)
        v2 = Vector(1, 2)
        self.assertEqual(Vector(5, 7), (v1 + v2))

    def test_case_4(self):
        self.assertTrue(hasattr(Vector, '__sub__'))
        v1 = Vector(4, 5)
        v2 = Vector(1, 2)
        self.assertEqual(Vector(3, 3), (v1 - v2))

    def test_case_5(self):
        self.assertTrue(hasattr(Vector, '__mul__'))
        v1 = Vector(3, 4)
        v2 = Vector(2, 7)
        self.assertEqual(34, v1 * v2)
