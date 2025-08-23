# This is an input class. Do not edit.
from collections import deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    # Write your code here.
    sum_of_all_nodes = getTreeSum(tree)
    temp_sum = 0
    answer = 0
    flag = False

    def in_order_traversal(tree):
        nonlocal temp_sum
        nonlocal answer
        nonlocal flag

        if not tree:
            return

        in_order_traversal(tree.left)

        temp_sum += tree.value

        if sum_of_all_nodes == temp_sum * 2:
            flag = True
            answer = temp_sum
            return temp_sum

        in_order_traversal(tree.right)

        return temp_sum

    in_order_traversal(tree)

    return answer

def getTreeSum(tree):

    queue = deque()
    summ = 0
    queue.append(tree)

    while queue:
        current = queue.popleft()
        summ += current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return summ
