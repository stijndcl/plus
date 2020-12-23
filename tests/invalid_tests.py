import random
import unittest
from plus.plus import plus


class TestInvalid(unittest.TestCase):
    def testNegative(self):
        # First negative
        self.assertRaises(AssertionError, plus, -1, 0)
        self.assertRaises(AssertionError, plus, -1, 10)

        # Second negative
        self.assertRaises(AssertionError, plus, 0, -1)
        self.assertRaises(AssertionError, plus, 10, -1)

        # Both negative
        self.assertRaises(AssertionError, plus, -1, -1)
        self.assertRaises(AssertionError, plus, -10, -10)

    def testNotInt(self):
        # Floats
        first = random.uniform(0, 99.9)
        second = random.uniform(0, 99.9)

        self.assertRaises(AssertionError, plus, first, second)
        self.assertRaises(AssertionError, plus, second, first)

        # Strings
        self.assertRaises(AssertionError, plus, "Test string", 17)
        self.assertRaises(AssertionError, plus, 71, "123456")


if __name__ == '__main__':
    unittest.main()
