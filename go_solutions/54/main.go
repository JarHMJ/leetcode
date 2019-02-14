package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
	var result []int
	h := len(matrix)
	if h == 0 {
		return result
	}
	l := len(matrix[0])
	left := 0
	top := 0
	right := l - 1
	bottom := h - 1
	i := 0
	j := 0
	fx := 1
	for a := l * h; a > 0; a-- {
		fmt.Printf("i:%d j:%d v:%d", i, j, matrix[i][j])

		result = append(result, matrix[i][j])
		switch fx {
		case 1:
			fmt.Printf("fx:%d", fx)
			fmt.Print("\n")
			if j == right {
				fx = 2
				top++
				i++
			} else {
				j++
			}
		case 2:
			fmt.Printf("fx:%d", fx)
			fmt.Print("\n")
			if i == bottom {
				fx = 3
				j--
				right--
			} else {
				i++
			}
		case 3:
			fmt.Printf("fx:%d", fx)
			fmt.Print("\n")
			if j == left {
				fx = 4
				i--
				bottom--
			} else {
				j--
			}
		case 4:
			fmt.Printf("fx:%d", fx)
			fmt.Print("\n")
			if i == top {
				fx = 1
				j++
				left++
			} else {
				i--
			}
		}
	}
	return result
}

func main() {
	//matrix := [][]int{
	//	{1, 2, 3, 10},
	//	{4, 5, 6, 11},
	//	{7, 8, 9, 12},
	//	{13, 14, 15, 16}}
	var matrix [][]int
	result := spiralOrder(matrix)
	fmt.Print(result)
}
