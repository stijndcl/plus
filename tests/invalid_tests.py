import random
import unittest
from plus.plus import plus


class TestInvalid(unittest.TestCase):
    def testNegative(self):
        # First negative
        self.assertRaises(ValueError, plus, -1, 0)
        self.assertRaises(ValueError, plus, -1, 10)

        # Second negative
        self.assertRaises(ValueError, plus, 0, -1)
        self.assertRaises(ValueError, plus, 10, -1)

        # Both negative
        self.assertRaises(ValueError, plus, -1, -1)
        self.assertRaises(ValueError, plus, -10, -10)

    def testNotInt(self):
        # Floats
        first = random.uniform(0, 99.9)
        second = random.uniform(0, 99.9)

        self.assertRaises(TypeError, plus, first, second)
        self.assertRaises(TypeError, plus, second, first)

        # Strings
        self.assertRaises(TypeError, plus, "Test string", 17)
        self.assertRaises(TypeError, plus, 71, "123456")


if __name__ == '__main__':
    unittest.main()
