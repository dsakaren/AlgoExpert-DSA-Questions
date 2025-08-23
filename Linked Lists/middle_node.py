# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    node_len = countNodes(linkedList)
    idx = node_len // 2
    current = linkedList

    while current:
        if idx == 0:
            print(current.value)
            return current
        current = current.next
        idx -= 1


def countNodes(linkedList):
    count = 0
    current = linkedList

    while current:
        count += 1
        current = current.next

    return count
