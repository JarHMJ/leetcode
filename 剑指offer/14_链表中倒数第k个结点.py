# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        pre = head
        for _ in range(k - 1):
            if head.next:
                head = head.next
            else:
                return None

        while head.next:
            head = head.next
            pre = pre.next
        return pre
