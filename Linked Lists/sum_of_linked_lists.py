# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    str1 = ''
    str2 = ''
    str1_reversed = ''
    str2_reversed = ''

    current1 = linkedListOne
    current2 = linkedListTwo

    while current1:
        str1 += str(current1.value)
        current1 = current1.next

    while current2:
        str2 += str(current2.value)
        current2 = current2.next

    str1_reversed = str1[::-1]
    str2_reversed = str2[::-1]

    result = int(str1_reversed) + int(str2_reversed)

    return create_new_list(str(result))

def create_new_list(result):
    head = LinkedList(int(result[-1]))
    current = head
    for i in range(len(result) - 2, -1, -1):
        current.next = LinkedList(int(result[i]))
        current = current.next
    return head

