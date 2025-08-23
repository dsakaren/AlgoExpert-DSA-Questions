# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
    balanced = True

    def height(root):
        nonlocal balanced
        if not root:
            return 0

        left_height = height(root.left)
        if not balanced:
            return 0

        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            balanced = False
            return 0

        return 1 + max(left_height, right_height)

    height(tree)
    return balanced
