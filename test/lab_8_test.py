import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from lab_8_main import read_graph_from_txt, max_flow


class TestFlowerDelivery(unittest.TestCase):
    def test_manual_graph(self):
        farms, shops, capacity = read_graph_from_txt("C:/Users/User/Desktop/work/roads.txt")
        result = max_flow(farms, shops, capacity)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
