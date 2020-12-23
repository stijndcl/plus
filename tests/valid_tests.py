import unittest
import random
from plus import plus


class TestValid(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(plus(1, 0), 1)
        self.assertEqual(plus(0, 1), 1)
        self.assertEqual(plus(0, 0), 0)

    def testOneZero(self):
        self.assertEqual(plus(10, 0), 10)
        self.assertEqual(plus(0, 10), 10)

    def testRandomNumbers(self):
        for _ in range (25):
            first = random.randint(0, 250)
            second = random.randint(0, 250)
            self.assertEqual(plus(first, second), sum([first, second]))  # Intentionally not using + here


if __name__ == '__main__':
    unittest.main()
