"""
https://www.geeksforgeeks.org/reverse-a-linked-list/
Given pointer to the head node of a linked list, the task is to reverse the linked list.
 We need to reverse the list by changing the links between nodes.

 Input: Head of following linked list
1->2->3->4->NULL
Output: Linked list should be changed to,
4->3->2->1->NULL
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def print(self):
        node = self.head
        while node is not None:
            print( node.data, end = " -> ")
            node = node.next

    def prepareLnkList(self, arr, leng):
        for i in range(leng):
            self.add(arr[i])


    def reverse(self, head):
        if  head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def reverse_loop(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

arr = [3,2,5,7,6,7,5,4,9]
leng = len(arr)
lnkList = LinkedList()
lnkList.prepareLnkList(arr,leng)
#lnkList.print()
head = lnkList.reverse(lnkList.head)
lnkList.head = head
#lnkList.reverse_loop()
lnkList.print()