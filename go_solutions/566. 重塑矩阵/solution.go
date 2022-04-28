package solution

func matrixReshape(mat [][]int, r int, c int) [][]int {
	if len(mat) == 0 {
		return mat
	}

	if len(mat)*len(mat[0]) != r*c {
		return mat
	}

	result := make([][]int, r)
	for i := 0; i < r; i++ {
		result[i] = make([]int, c)
	}

	i, j := 0, 0

	for _, ints := range mat {
		for _, v := range ints {
			result[i][j] = v

			if j == c-1 {
				i++
				j = 0
				continue
			}
			j++
		}
	}
	return result
}
