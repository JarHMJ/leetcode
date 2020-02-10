package main

import "fmt"

func findKthLargest(nums []int, k int) int {
	k--
	for l, h := 0, len(nums)-1; l < h; {
		p := partition(nums, l, h)
		if k == p {
			break
		} else if k < p {
			h = p - 1
		} else if k > p {
			l = p + 1
		}
	}
	return nums[k]
}

func partition(nums []int, l, h int) int {
	i := l
	tmp := nums[h]
	for ; l <= h; l++ {
		if nums[l] > tmp {
			nums[l], nums[i] = nums[i], nums[l]
			i++
		}
	}
	nums[i], nums[h] = tmp, nums[i]
	return i
}

func main() {
	fmt.Println(findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4))
}
