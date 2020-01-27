package main

func numberOfArithmeticSlices(A []int) int {
	dp, sum := 0, 0
	for i := 2; i < len(A); i++ {
		if A[i]-A[i-1] == A[i-1]-A[i-2] {
			dp += 1
			sum += dp
		} else {
			dp = 0
		}
	}
	return sum
}
