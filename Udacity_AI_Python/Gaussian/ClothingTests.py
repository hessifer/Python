# Unit tests to check your solution

import unittest
from Clothing import Clothing
from Clothing import Blouse
from Clothing import Pants


class TestClothingClass(unittest.TestCase):
    def setUp(self):
        self.clothing = Clothing('orange', 'M', 'stripes', 35)
        self.blouse = Blouse('blue', 'M', 'luxury', 40, 'Brazil')
        self.pants = Pants('black', 32, 'baggy', 60, 30)

    def test_initialization(self):
        self.assertEqual(self.clothing.color, 'orange', 'color should be \
                         orange')
        self.assertEqual(self.clothing.price, 35, 'incorrect price')

        self.assertEqual(self.blouse.color, 'blue', 'color should be blue')
        self.assertEqual(self.blouse.size, 'M', 'incorrect size')
        self.assertEqual(self.blouse.style, 'luxury', 'incorrect style')
        self.assertEqual(self.blouse.price, 40, 'incorrect price')
        self.assertEqual(self.blouse.country_of_origin, 'Brazil', 'incorrect \
                         country of origin')

    def test_calculateshipping(self):
        self.assertEqual(self.clothing.calculate_shipping(.5, 3), .5 * 3,
                         'Clothing shipping calculation not as expected')
        self.assertEqual(self.blouse.calculate_shipping(.5, 3), .5 * 3,
                         'Clothing shipping calculation not as expected')


tests = TestClothingClass()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)
