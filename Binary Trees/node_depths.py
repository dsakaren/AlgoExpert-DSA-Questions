from collections import deque
def nodeDepths(root):
    # Write your code here.
    total_sum = 0
    queue = deque()
    queue.append((root, 0))

    while queue:
        current_node, current_value = queue.popleft()

        total_sum += current_value

        if current_node.left:
            queue.append((current_node.left, current_value + 1))

        if current_node.right:
            queue.append((current_node.right, current_value + 1))

    return total_sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
