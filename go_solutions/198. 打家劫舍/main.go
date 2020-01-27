package main

import "math"

func rob(nums []int) int {
	l := len(nums)
	var pre2, pre1 float64 = 0,0
	for i := 0;i<l;i++ {
		pre2, pre1 = math.Max(pre1 + float64(nums[i]), pre2), pre2
	}
	return int(pre2)
}
