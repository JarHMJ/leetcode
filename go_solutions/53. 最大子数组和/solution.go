package solution

//maxSubArray 暴力解 会超时
func maxSubArray(nums []int) int {
	max := nums[0]
	l := len(nums)
	for i := 0; i < l; i++ {
		sum := 0
		for j := i; j < l; j++ {
			if sum += nums[j]; sum > max {
				max = sum
			}
		}
	}
	return max
}

//maxSubArray1 动态规划
func maxSubArray1(nums []int) int {
	max := nums[0]
	l := len(nums)
	dp := max
	for i := 1; i < l; i++ {
		if dp+nums[i] > nums[i] {
			dp = dp + nums[i]
		} else {
			dp = nums[i]
		}
		if dp > max {
			max = dp
		}

	}
	return max
}

//maxSubArray2 贪心算法
func maxSubArray2(nums []int) int {
	max := nums[0]
	l := len(nums)
	sum := 0
	for i := 0; i < l; i++ {
		sum += nums[i]
		// 全局最优解为最大的连续和
		if sum > max {
			max = sum
		}
		// 局部最优解为当和小于0时，则开始重新计算
		if sum < 0 {
			sum = 0
		}
	}
	return max
}
