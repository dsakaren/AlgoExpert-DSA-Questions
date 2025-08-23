# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if not tree1 and not tree2:
        return None

    v1 = tree1.value if tree1 else 0
    v2 = tree2.value if tree2 else 0

    new_tree = BinaryTree(v1 + v2)

    new_tree.left = mergeBinaryTrees(tree1.left if tree1 else None, tree2.left if tree2 else None)
    new_tree.right = mergeBinaryTrees(tree1.right if tree1 else None, tree2.right if tree2 else None)

    return new_tree
