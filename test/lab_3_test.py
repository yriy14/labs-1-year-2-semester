import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from lab_3_code import BinaryTree, invert_binary_tree

class TestInvertBinaryTree(unittest.TestCase):
    def tree_to_list(self, root):
        if root is None:
            return []
        
        queue = [root]
        result = []
        front = 0  
        rear = 1  
        
        while front < rear:
            node = queue[front]
            front += 1
            if node is not None:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
                rear += 2
            else:
                result.append(None)
        
        while len(result) > 0 and result[len(result) - 1] is None:
            result.pop()
        
        return result
    
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        
        inverted_root = invert_binary_tree(root)
        expected_output = [1, 3, 2, 7, 6, 5, 4]
        self.assertEqual(self.tree_to_list(inverted_root), expected_output)

if __name__ == "__main__":
    unittest.main()
