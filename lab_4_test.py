import unittest
from lab_4_code import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_queue_operations(self):
        pq = PriorityQueue()
        pq.insert("A", 2)
        pq.insert("B", 5)
        pq.insert("C", 1)

        self.assertEqual(pq.view(), [("C", 1), ("A", 2), ("B", 5)])
        self.assertEqual(pq.pop(), ("B", 5))
        self.assertEqual(pq.pop(), ("A", 2))
        self.assertEqual(pq.pop(), ("C", 1))
        self.assertIsNone(pq.pop())


if __name__ == "__main__":
    unittest.main()
