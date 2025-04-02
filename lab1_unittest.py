import unittest
from lab1 import find_k_largest

class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        self.assertNotEqual(find_k_largest(arr, 3), (42, 6))
        self.assertEqual(find_k_largest(arr, 1), (42, 6))
        self.assertEqual(find_k_largest(arr, 5), (15, 0))
        self.assertEqual(find_k_largest(arr, 8), (2, 5))
        
    def test_invalid_k(self):
        arr = [10, 20, 30]
        with self.assertRaises(ValueError):
            find_k_largest(arr, 0)
        with self.assertRaises(ValueError):
            find_k_largest(arr, 4)

if __name__ == "__main__":
    unittest.main()

