package main

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	res := make([][]int, 0)
	dfs(candidates, nil, target, 0, &res)
	return res
}

func dfs(candidates, nums []int, target, left int, res *[][]int) {
	if target == 0 {
		tmp := make([]int, len(nums))
		copy(tmp, nums)
		*res = append(*res, tmp)
		return
	}

	for i := left; i < len(candidates); i++{
		if i != left && candidates[i] == candidates[i-1] { // *同层节点 数值相同，剪枝
			continue
		}
		if target < candidates[i] {
			return
		}
		dfs(candidates, append(nums, candidates[i]), target-candidates[i], i+1, res)
	}
}

