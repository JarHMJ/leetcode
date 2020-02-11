package main

import "fmt"

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, v := range nums {
		freqMap[v]++
	}
	bucket := make([][]int, len(nums)+1)
	for k, v := range freqMap {
		tmp := bucket[v]
		if tmp == nil {
			tmp = []int{k}
		} else {
			tmp = append(tmp, k)
		}
		bucket[v] = tmp

	}
	result := make([]int, 0, k)
loop:
	for i := len(nums); len(result) < k; i-- {
		tmp := bucket[i]
		if tmp == nil {
			continue
		}
		for _, v := range tmp {
			if len(result) >= k {
				goto loop
			}
			result = append(result, v)
		}
	}
	return result
}

func main() {
	fmt.Println(topKFrequent([]int{1,2}, 2))
}