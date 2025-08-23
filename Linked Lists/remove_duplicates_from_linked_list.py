# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    previous = head
    current = head.next

    while current:
        # print(current.value)
        if previous.value < current.value:
            previous = current
            current = current.next
            continue
        next = current.next
        previous.next = next
        current = next

    # temp = head
    # while temp:
    #     print(temp.value)
    #     temp = temp.next

    return head
