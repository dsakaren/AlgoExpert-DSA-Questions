# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    longest_diameter = [0]

    def height(root):
        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        diameter = left_height + right_height
        longest_diameter[0] = max(longest_diameter[0], diameter)
        
        return 1 + max(left_height, right_height)

    height(tree)
    return longest_diameter[0]
