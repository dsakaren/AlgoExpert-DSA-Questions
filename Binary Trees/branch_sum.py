# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []

    def dfs(node, running_sum):
        if node is None:
            return

        new_running_sum = running_sum + node.value

        if node.left is None and node.right is None:
            sums.append(new_running_sum)
            return

        dfs(node.left, new_running_sum)
        dfs(node.right, new_running_sum)

    dfs(root, 0)

    return sums
