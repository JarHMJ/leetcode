package solution

func intersect(nums1 []int, nums2 []int) []int {
	short := nums1
	long := nums2
	// 找出较短的数组
	if len(nums1) > len(nums2) {
		short = nums2
		long = nums1
	}
	s := len(short)
	l := len(long)

	numsMap := make(map[int]int)
	result := []int{}

	// 双指针
	i, j := 0, 0
	for i < s && j < l {
		target := short[i]
		// 相等两个指针同时往后移一位
		if target == long[j] {
			result = append(result, target)
			i++
			j++
		} else { // 不相等再从map中查找
			sum := numsMap[target]
			if sum > 0 { // 找到
				result = append(result, target)
				numsMap[target]--
				i++
			} else { // 没找到，怎把long中的数据放入map中
				numsMap[long[j]]++
				j++
			}
		}
	}
	// 把short中的遍历完
	for i < s {
		target := short[i]
		sum := numsMap[target]
		if sum > 0 {
			result = append(result, target)
			numsMap[target]--
		}
		i++
	}

	return result
}

func intersect1(nums1 []int, nums2 []int) []int {
	if len(nums1) > len(nums2) {
		return intersect(nums2, nums1)
	}
	m := map[int]int{}
	for _, num := range nums1 {
		m[num]++
	}

	intersection := []int{}
	for _, num := range nums2 {
		if m[num] > 0 {
			intersection = append(intersection, num)
			m[num]--
		}
	}
	return intersection
}
