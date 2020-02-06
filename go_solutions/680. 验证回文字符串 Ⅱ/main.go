package main

func validPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; {
		if s[i] != s[j] {
			return helper(&s, i+1, j) || helper(&s, i, j-1)
		} else {
			i++
			j--
		}
	}
	return true
}

func helper(s *string, l, r int) bool {
	for l < r {
		if (*s)[l] == (*s)[r] {
			l++
			r--
		} else {
			return false
		}
	}
	return true
}

func main() {
	validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
}
