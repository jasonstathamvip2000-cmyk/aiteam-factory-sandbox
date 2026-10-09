import unittest

from app import add, power


class TestAdd(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add(2, 0), 2)


class T(unittest.TestCase):
    """Tests for power."""

    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(5, 0), 1)
        with self.assertRaises(ValueError):
            power(2, -1)


if __name__ == "__main__":
    unittest.main()

