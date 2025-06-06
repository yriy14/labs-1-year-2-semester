class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None
    
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    
    return tree