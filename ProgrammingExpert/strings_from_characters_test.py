# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

import strings_from_characters


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
        string1 = "hello"
        string2 = "world"
        expected = 1
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_2(self):
        frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
        string1 = "hello"
        string2 = "world"
        expected = 1
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_3(self):
        frequencies = {"a": 3, "b": 5, "c": 3, "d": 2, "e": 1}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 2
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_4(self):
        frequencies = {"a": 3, "b": 1, "c": 3, "d": 2, "e": 1}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 0
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_5(self):
        frequencies = {}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 0
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_6(self):
        frequencies = {}
        string1 = ""
        string2 = ""
        expected = 2
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

    def test_case_7(self):
        frequencies = {"a": 1}
        string1 = ""
        string2 = ""
        expected = 2
        self.assertEqual(strings_from_characters.create_strings_from_characters(frequencies, string1, string2), expected)

if __name__ == '__main__':
    unittest.main()