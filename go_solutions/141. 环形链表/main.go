package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	fastHead := head.Next
	for fastHead != nil && head != nil && fastHead.Next != nil {
		if fastHead == head {
			return true
		}
		fastHead = fastHead.Next.Next
		head = head.Next
	}
	return false
}
