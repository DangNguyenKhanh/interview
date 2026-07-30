class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = Node(10)
node2 = Node(20)
node1.next = node2
