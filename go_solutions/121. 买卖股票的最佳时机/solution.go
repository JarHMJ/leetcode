package solution

func maxProfit(prices []int) int {
	dp := prices[0]
	max := 0
	for i := 1; i < len(prices); i++ {
		if prices[i-1] < dp {
			dp = prices[i-1]
		}

		tmp := prices[i] - dp
		if tmp > max {
			max = tmp
		}
	}
	return max
}
