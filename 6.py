def sum_left_leaves(root):
    if root is None:
        return 0
    sum = 0
    if root.left is not None and root.left.left is None:
        return 