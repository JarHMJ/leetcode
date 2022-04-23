package solution

//twoSum 暴力解法
func twoSum(nums []int, target int) []int {
	l := len(nums)
	result := []int{0, 0}
Loop:
	for i := 0; i < l; i++ {
		for j := i + 1; j < l; j++ {
			if nums[i]+nums[j] == target {
				result = []int{i, j}
				break Loop
			}
		}
	}
	return result
}

//twoSum hash表
func twoSum1(nums []int, target int) []int {
	result := []int{0, 0}
	hashmap := make(map[int]int)
	for i, num := range nums {
		search := target - num
		if l, ok := hashmap[search]; ok {
			result = []int{l, i}
			break
		}
		hashmap[num] = i
	}
	return result
}
