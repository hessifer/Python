# This suite of tests is written to run against your code
# so that we can check its correctness.

import inspect
import unittest

from temperature_class import Temperature


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(inspect.isclass(Temperature), "Temperature should be a class.")

    def test_case_2(self):
        self.assertTrue(hasattr(Temperature, "update_max_temperature"),
                        "Temperature should have a `update_max_temperature` method.")
        self.assertTrue(hasattr(Temperature, "update_min_temperature"),
                        "Temperature should have a `update_min_temperature` method.")

    def test_case_3(self):
        temperature = Temperature(60)
        Temperature.update_max_temperature(100)
        with self.assertRaisesRegexp(Exception, "Invalid temperature"):
            bad_temperature = Temperature(110)

    def test_case_4(self):
        Temperature.update_min_temperature(5)
        with self.assertRaisesRegexp(Exception, "Invalid temperature"):
            bad_temperature = Temperature(4)

    def test_case_5(self):
        with self.assertRaisesRegexp(Exception, "Invalid temperature"):
            Temperature.update_min_temperature(1000)

    def test_case_6(self):
        with self.assertRaisesRegexp(Exception, "Invalid temperature"):
            Temperature.update_max_temperature(-1000)


if __name__ == "__main__":
    unittest.main()

