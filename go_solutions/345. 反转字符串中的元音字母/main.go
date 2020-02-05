package main

var vowels = map[rune]struct{}{
	'a': struct{}{},
	'e': struct{}{},
	'i': struct{}{},
	'o': struct{}{},
	'u': struct{}{},
	'A': struct{}{},
	'E': struct{}{},
	'I': struct{}{},
	'O': struct{}{},
	'U': struct{}{},
}

func reverseVowels(s string) string {
	chars := []rune(s)
	for i, j := 0, len(chars)-1; ; {
		for i < j && !isVowel(chars[i]) {
			i++
		}
		for i < j && !isVowel(chars[j]) {
			j--
		}
		if i >= j {
			break
		}
		chars[i], chars[j] = chars[j], chars[i]
		i++
		j--
	}
	return string(chars)

}

func isVowel(s rune) bool {
	_, ok := vowels[s]
	return ok
}

func main() {
	reverseVowels("asdasasds")
}
