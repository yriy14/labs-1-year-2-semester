class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.priority > current.priority:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def pop(self):
        if self.root is None:
            return None
        parent = None
        current = self.root
        while current.left is not None:
            parent = current
            current = current.left
        if parent is None:
            self.root = self.root.right
        else:
            parent.left = current.right
        return (current.value, current.priority)

    def view(self):
        result = []
        self._inorder(self.root, result)
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if result[i][1] > result[j][1]:
                    temp = result[i]
                    result[i] = result[j]
                    result[j] = temp
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append((node.value, node.priority))
            self._inorder(node.right, result)


