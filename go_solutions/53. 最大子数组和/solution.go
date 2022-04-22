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
