from collections import deque

def bfs(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def dfs(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)