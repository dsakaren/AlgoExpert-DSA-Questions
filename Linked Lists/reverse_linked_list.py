# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    previous = None
    current = head
    while current:
        # print(current.value)
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
