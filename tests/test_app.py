import unittest

from app import add


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)

    def test_sum(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
