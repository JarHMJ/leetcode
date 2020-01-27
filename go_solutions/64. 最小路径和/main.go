package main

import (
	"math"
)

func minPathSum(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	if n == 0 {
		return 0
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				grid[i][j] = grid[i][j]
			} else if i == 0 {
				grid[i][j] = grid[i][j-1] + grid[i][j]
			} else if j == 0 {
				grid[i][j] = grid[i-1][j] + grid[i][j]
			} else {
				grid[i][j] = grid[i][j] + int(math.Min(float64(grid[i-1][j]), float64(grid[i][j-1])))
			}
		}
	}
	return grid[m-1][n-1]
}

func main() {
	a := [][]int{{1, 2, 5}, {3, 2, 1}}
	minPathSum(a)
}
