import unittest
from lab_8_main import read_graph_from_txt, max_flow


class TestFlowerDelivery(unittest.TestCase):
    def test_manual_graph(self):
        farms, shops, capacity = read_graph_from_txt("C:/Users/Admin/OneDrive/Desktop/lab_8/roads.txt")
        result = max_flow(farms, shops, capacity)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
