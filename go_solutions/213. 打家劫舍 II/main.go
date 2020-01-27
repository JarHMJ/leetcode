package main

import "math"

func rob(nums []int) int {
	l := len(nums)
	switch l {
	case 0:
		return 0
	case 1:
		return nums[0]
	default:
		return int(math.Max(robInner(nums, 0, l-1), robInner(nums, 1, l)))
	}

}

func robInner(nums []int, first, last int) float64 {
	var pre2, pre1 float64 = 0, 0
	for i := first; i < last; i++ {
		pre2, pre1 = math.Max(pre1+float64(nums[i]), pre2), pre2
	}
	return pre2
}
