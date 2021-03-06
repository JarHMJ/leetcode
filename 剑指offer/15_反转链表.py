# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        pre = pHead
        cur = pHead.next

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        pHead.next = None
        return pre