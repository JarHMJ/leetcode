package main

import (
	"math"
)

func integerBreak(n int) int {
	dp := make([]int, n+1)
	dp[2] = 1
	for i := 3; i <= n; i++ {
		for j := 1; j <= i-1; j++ {
			dp[i] = int(math.Max(float64(dp[i]), math.Max(float64(j*(i-j)), float64(j*dp[i-j]))))
		}
	}
	return dp[n]
}
