class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_link = ListNode(0)
        rim = 0
        res = temp_link
        while l1 or l2 or rim > 0:
            if l1 and l2:
                temp_link.val = (l1.val + l2.val + rim) % 10
                rim = int((l1.val + l2.val + rim) / 10)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                temp_link.val = (l1.val + rim) % 10
                rim = int((l1.val + rim) / 10)
                l1 = l1.next
            elif l2:
                temp_link.val = (l2.val + rim) % 10
                rim = int((l2.val + rim) / 10)
                l2 = l2.next
            elif rim > 0:
                temp_link.val = rim
                rim = 0
            if l1 or l2 or rim > 0:
                temp_link.next = ListNode(0)
                temp_link = temp_link.next
        return res