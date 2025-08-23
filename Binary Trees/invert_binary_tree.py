from collections import deque
def invertBinaryTree(tree):
    # Write your code here.
    queue = deque()
    queue.append(tree)

    while queue:
        current = queue.popleft()
        if current is None:
            continue
        swipe_values(current)
        queue.append(current.left)
        queue.append(current.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def swipe_values(tree):
    tree.left, tree.right = tree.right, tree.left