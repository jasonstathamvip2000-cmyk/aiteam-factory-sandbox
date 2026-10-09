import unittest

from app import add, square


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)


class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)


if __name__ == "__main__":
    unittest.main()
