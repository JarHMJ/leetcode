package main

func uniquePaths(m int, n int) int {
	if m < 1 || n < 1 {
		return 0
	}
	dp := make([]int, n)
	dp[0] = 1
	for j := 0; j < m; j++ {
		for i := 0; i < n; i++ {
			if i == 0 {
				dp[i] = dp[i]
			} else {
				dp[i] = dp[i-1] + dp[i]
			}
		}
	}
	return dp[n-1]
}
