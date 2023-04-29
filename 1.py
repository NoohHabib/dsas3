class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def _init_(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                curr = q.pop(0)
                if curr.left is None:
                    curr.left = node
                    break
                elif curr.right is None:
                    curr.right = node
                    break
                else:
                    q.append(curr.left)
                    q.append(curr.right)

    def print_level_order(self):
        if self.root is None:
            return
        q = [self.root]
        while len(q) > 0:
            print(q[0].data, end=' ')
            curr = q.pop(0)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.data, end=' ')
            self.print_inorder(node.right)

    def print_preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        if node is not None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data, end=' ')