# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = deque([])
        queue.append(self)
        while queue:
            current_node = queue.popleft()
            array.append(current_node.name)
            for child in current_node.children:
                queue.append(child)
        return array
