"""
https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

Example 1:

Input:
N = 3
value[] = {1,3,4}
x = 2
Output: True
Explanation: In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
Successful implement

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def prepareLnkList(self, arr, leng, cirNode ):
        lnkList = LinkList()
        lnkList.add(arr[0])
        tail = lnkList.head
        for i in range(1,leng):
            lnkList.add(arr[i])
            if i == cirNode -1:
                cirLink = lnkList.head
        tail.next = cirLink
        return lnkList

    def detectLoop(self, head):
        slwPnt = head
        if slwPnt.next == None:
            return False
        fstPnt = head
        while slwPnt is not None and fstPnt is not None:
            slwPnt = slwPnt.next
            fstPnt = fstPnt.next
            if fstPnt is not None:
                fstPnt = fstPnt.next
            if slwPnt == fstPnt:
                return True
        return False

leng= 3
arr = [1,3,4,6,7,8,5,6,7,3,4,6]
cirNode = 3
lnkList = LinkList()
head = lnkList.prepareLnkList(arr,leng,cirNode)
print(lnkList.detectLoop(head.head))