# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    values = {}

    current1 = linkedListOne
    current2 = linkedListTwo

    while current1:
        if current1.value not in values:
            values[current1.value] = current1
        current1 = current1.next

    while current2:
        if current2.value in values:
            # print(current2.value)
            return values[current2.value]
        current2 = current2.next

    return None
