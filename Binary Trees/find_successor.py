# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    return_next = [False]
    result = [None]

    def inorderTraversal(root):
        # Base case: if null
        if root is None:
            return
        inorderTraversal(root.left)

        if return_next[0]:
            result[0] = root
            return_next[0] = False
            return
        if root == node:
            return_next[0] = True

        inorderTraversal(root.right)
        
    inorderTraversal(tree)
    return result[0]
