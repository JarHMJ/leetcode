package main

import "math"

func judgeSquareSum(c int) bool {
	i, j := 0, int(math.Sqrt(float64(c)))
	for i <= j {
		sum := i*i + j*j
		switch {
		case sum == c:
			return true
		case sum < c:
			i++
		case sum > c:
			j--
		}
	}
	return false
}
