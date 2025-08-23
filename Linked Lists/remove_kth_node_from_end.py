# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    len_of_linked_list = get_len_linked_list(head)

    if k == len_of_linked_list:
        head.value = head.next.value
        head.next = head.next.next
        return

    idx_to_remove = len_of_linked_list - k
    current = head

    while current:
        if idx_to_remove == 1:
            current.next = current.next.next
            break
        current = current.next
        idx_to_remove -= 1
    pass

def get_len_linked_list(head):

    current = head
    count = 0

    while current:
        count += 1
        current = current.next

    return count
