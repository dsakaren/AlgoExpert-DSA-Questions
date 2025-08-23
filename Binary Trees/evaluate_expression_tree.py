# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    operations = {
        -1 : int.__add__,
        -2 : int.__sub__,
        -3 : lambda a, b: int(a / b),
        -4 : int.__mul__
    }

    op = operations.get(tree.value)

    if not op:
        return tree.value

    return op(evaluateExpressionTree(tree.left), evaluateExpressionTree(tree.right))
