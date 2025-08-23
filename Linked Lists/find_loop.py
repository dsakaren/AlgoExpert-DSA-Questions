# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    current_node = head

    while current_node:
        next_current_node = current_node.next
        temp = next_current_node
        while next_current_node:
            if next_current_node.value == current_node.value:
                print(current_node.value)
                return current_node
            next_current_node = next_current_node.next
            if next_current_node == temp:
                break

        current_node = current_node.next

    return None
