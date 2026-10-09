import unittest

from app import add, multiply


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
