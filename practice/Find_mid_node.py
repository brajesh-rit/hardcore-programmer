"""
https://www.geeksforgeeks.org/python-program-to-find-middle-of-a-linked-list-using-one-traversal/
Finding middle node in a Linked List in O(N) time and Single Pass (with CODE illustration)
This video shows both the Naive and Efficient algorithm to find middle node in a linked list.
It covers O(N) time complexity and a single pass algorithm. This video also shows the Code Demo of the program.
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        NewNode = Node(val)
        NewNode.nxt = self.head
        self.head = NewNode

    def PrintMiddle(self):
        slowPtr = self.head
        fastPtr = self.head

        if self.head is not None:
            while (fastPtr is not None and slowPtr is not None):
                slowPtr = slowPtr.nxt
                fastPtr = fastPtr.nxt
                if fastPtr is not None:
                    fastPtr = fastPtr.nxt
            print("Middle element is :", slowPtr.val)



list = LinkedList()

#list.add(9)
#list.add(8)
#list.add(7)

#list.add(6)
list.add(5)

list.add(4)
list.add(3)
list.add(2)
list.add(1)
list.PrintMiddle()
