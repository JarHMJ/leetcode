# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[ListNode], start: int, end: int):
        if start == end:
            return lists[start]
        if start > end:
            return None

        mid = start + (end - start) // 2
        left = self.merge(lists, start, mid)
        right = self.merge(lists, mid + 1, end)
        return self.merge2lists(left, right)

    def merge2lists(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = ptr = l1
            l1 = l1.next
        else:
            head = ptr = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next

        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2

        return head
