package main

import "fmt"

func findLongestWord(s string, d []string) string {
	sLen := len(s)
	result := ""
	for _, subStr := range d {
		l := len(subStr)
		if l > sLen {
			continue
		}
		j := 0
		for i := 0; i < sLen && j < l; i++ {
			if s[i] == subStr[j] {
				j++
			}
		}
		if j == l {
			if len(result) < l {
				result = subStr
			} else if len(result) == l && subStr < result {
				result = subStr
			}
		}
	}
	return result
}

func main() {
	fmt.Println(findLongestWord("abpcplea", []string{"ale", "apple", "monkey", "plea"}))
}
