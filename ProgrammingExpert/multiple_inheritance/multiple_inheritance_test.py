# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

from multiple_inheritance import Animal, Mammal, Reptile, Monkey, Lizard


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        animal = Animal(10, 50, 1.5)
        self.assertEqual(10, animal.age)
        self.assertEqual(50, animal.weight)
        self.assertEqual(1.5, animal.height)

    def test_case_2(self):
        mammal = Mammal(10, 50, 1.5, "male")
        self.assertEqual(10, mammal.age)
        self.assertEqual(50, mammal.weight)
        self.assertEqual(1.5, mammal.height)
        self.assertEqual("male", mammal.sex)

    def test_case_3(self):
        monkey = Monkey(10, 50, 1.5, "male", "grey")
        self.assertEqual(10, monkey.age)
        self.assertEqual(50, monkey.weight)
        self.assertEqual(1.5, monkey.height)
        self.assertEqual("male", monkey.sex)
        self.assertEqual("grey", monkey.color)
        self.assertEqual(5, monkey.fingers)

    def test_case_4(self):
        lizard = Lizard(10, 50, 1.5, 0, "red")
        self.assertEqual(10, lizard.age)
        self.assertEqual(50, lizard.weight)
        self.assertEqual(1.5, lizard.height)
        self.assertEqual("red", lizard.color)
        self.assertEqual(True, lizard.tail)

    def test_case_5(self):
        self.assertIn(Animal, Mammal.__bases__)
        self.assertIn(Animal, Reptile.__bases__)
        self.assertIn(Mammal, Monkey.__bases__)
        self.assertIn(Reptile, Lizard.__bases__)

    def test_case_6(self):
        self.assertTrue(hasattr(Monkey, "fingers"),
                        "The Monkey class should have a static property `fingers`.")
        self.assertTrue(hasattr(Lizard, "tail"),
                        "The Lizard class should have a static property `tail`.")
        self.assertEqual(5, Monkey.fingers)
        self.assertEqual(True, Lizard.tail)


if __name__ == "__main__":
    unittest.main()
