import unittest

from stats import mean, median, mode, variance


class TestMean(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_single(self):
        self.assertEqual(mean([5]), 5)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            mean([])


class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_even_length(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])


class TestMode(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_tie_breaks_to_smallest(self):
        self.assertEqual(mode([1, 1, 2, 2]), 1)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            mode([])


class TestVariance(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(variance([1, 2, 3, 4]), 1.25)

    def test_constant_list(self):
        self.assertEqual(variance([5, 5, 5]), 0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            variance([])


if __name__ == "__main__":
    unittest.main()
