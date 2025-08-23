# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    # Write your code here.
    def dfs(root1: BinaryTree, root2: BinaryTree):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.value != root2.value:
            return False

        return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

    return dfs(tree, tree)
