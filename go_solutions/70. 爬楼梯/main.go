package main

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	pre1, pre2:= 2,1
	for i := 2; i < n; i++ {
		pre1, pre2 = pre1+pre2, pre1
	}
	return pre1
}
