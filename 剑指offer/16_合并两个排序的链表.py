# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            result = pHead1
            pHead1 = pHead1.next
        else:
            result = pHead2
            pHead2 = pHead2.next
        tmp = result
        while pHead1 or pHead2:
            if not pHead1:
                tmp.next = pHead2
                break
            if not pHead2:
                tmp.next = pHead1
                break
            if pHead1.val <= pHead2.val:
                tmp.next = pHead1
                tmp = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                tmp = pHead2
                pHead2 = pHead2.next
        return result

if __name__ == '__main__':
    test = Solution()
    pHead1 = ListNode(1)
    # pHead1.next = ListNode(3)
    # pHead1.next.next = ListNode(5)
    pHead2 = ListNode(2)
    # pHead2.next = ListNode(4)
    # pHead2.next.next = ListNode(6)
    result = test.Merge(pHead1, pHead2)
    while result:
        print result.val
        result = result.next

