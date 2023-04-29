class Node:
    def _init_(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_nodes(root):
    if root is None:
        return 0
    return root.value + sum_nodes(root.left) + sum_nodes(root.right)

# Example usage:
# tree = Node(10, Node(5, Node(3), Node(7)), Node(15, Node(12), Node(18)))
# print(sum_nodes(tree)) # Output: 70 (10+5+15+3+7+12+18)