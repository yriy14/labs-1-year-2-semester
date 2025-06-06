import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from lab_2_code import min_eating_speed

class TestBananaEating(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_eating_speed([3,6,7,11], 8), 4)
        self.assertEqual(min_eating_speed([30,11,23,4,20], 6), 23)

if __name__ == "__main__":
    unittest.main()