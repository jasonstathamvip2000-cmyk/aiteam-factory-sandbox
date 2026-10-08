import unittest

from app import add, subtract


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
