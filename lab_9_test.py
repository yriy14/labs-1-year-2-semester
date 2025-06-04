import unittest
from lab_9_code import build_chain

class TestWChain(unittest.TestCase):
    def test_example_1(self):
        words = [
            "crates", "car", "cats", "crate", "rate",
            "at", "ate", "tea", "rat", "a"
        ]
        self.assertEqual(build_chain(words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(build_chain(words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(build_chain(words), 1)

    def test_single_letter(self):
        self.assertEqual(build_chain(["a"]), 1)

    def test_no_chain(self):
        self.assertEqual(build_chain(["abc", "def", "ghi"]), 1)

if __name__ == "__main__":
    unittest.main()
