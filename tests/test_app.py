import unittest

from app import add, is_odd


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)


class TestIsOdd(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))


if __name__ == "__main__":
    unittest.main()

