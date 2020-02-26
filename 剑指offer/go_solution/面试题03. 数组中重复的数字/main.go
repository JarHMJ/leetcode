package main

func findRepeatNumber(nums []int) int {
	m := make(map[int]bool)
	for _, v := range nums {
		if _, ok := m[v]; ok {
			return v
		} else {
			m[v] = true
		}
	}
	return -1
}
