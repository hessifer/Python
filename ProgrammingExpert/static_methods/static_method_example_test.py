# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

from static_method_example import Physics


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(40, Physics.calculate_net_force(4, 10))
        self.assertEqual(0, Physics.calculate_net_force(0, 0))

    def test_case_2(self):
        self.assertEqual(2, Physics.calculate_acceleration(5, 10))
        self.assertEqual(4, Physics.calculate_acceleration(2.5, 10))

    def test_case_3(self):
        self.assertEqual(25, Physics.calculate_mass(50, 2))
        self.assertEqual(0, Physics.calculate_mass(0, 2))

    def test_case_4(self):
        self.assertEqual(0, Physics.calculate_net_force(-50, -2))
        self.assertEqual(0, Physics.calculate_acceleration(-5, 10))
        self.assertEqual(0, Physics.calculate_mass(-50, -2))

    def test_case_5(self):
        self.assertEqual(0, Physics.calculate_acceleration(0, 10))
        self.assertEqual(0, Physics.calculate_mass(50, 0))


if __name__ == "__main__":
    unittest.main()
