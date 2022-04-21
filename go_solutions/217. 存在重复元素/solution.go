package solution

func containsDuplicate(nums []int) bool {
	numsMap := make(map[int]struct{})
	for _, num := range nums {
		if _, ok := numsMap[num]; ok {
			return true
		} else {
			numsMap[num] = struct{}{}
		}
	}
	return false
}
