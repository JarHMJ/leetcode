# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        res = ListNode(0)
        r = res
        carry = 0
        while l1 or l2 or carry:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            sum = l1.val + l2.val + carry
            r.next = ListNode(sum % 10)
            r = r.next
            carry = sum // 10
            if isinstance(l1, ListNode):
                l1 = l1.next
            if isinstance(l2, ListNode):
                l2 = l2.next
        return res.next
