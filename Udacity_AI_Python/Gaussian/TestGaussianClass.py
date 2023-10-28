# Unit tests to check your solution

import unittest
import GaussianClassOrig as GC


class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = GC.Gaussian(25, 2)

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect \
                         standard deviation')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,
                         'pdf function does not give expected result')

    def test_meancalculation(self):
        self.gaussian.read_data_file('numbers.txt', True)
        self.assertEqual(self.gaussian.calculate_mean(), sum(
            self.gaussian.data) / float(len(self.gaussian.data)),
            'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.gaussian.read_data_file('numbers.txt', True)
        self.assertEqual(round(self.gaussian.stdev, 2), 92.87,
                         'sample standard deviation incorrect')
        self.gaussian.read_data_file('numbers.txt', False)
        self.assertEqual(round(self.gaussian.stdev, 2), 88.55,
                         'population standard deviation incorrect')

    def test_add(self):
        gaussian_one = GC.Gaussian(25, 3)
        gaussian_two = GC.Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

    def test_repr(self):
        gaussian_one = GC.Gaussian(25, 3)

        self.assertEqual(str(gaussian_one), "mean 25, standard deviation 3")


tests = TestGaussianClass()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)
