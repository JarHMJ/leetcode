package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	stack := make([]int, 0)
	for _, char := range tokens {
		switch char {
		case "+", "-", "*", "/":
			calculate(&stack, char)
		default:
			num, _ := strconv.Atoi(char)
			stack = append(stack, num)
		}
	}
	return stack[0]
}

func calculate(s *[]int, op string) {
	l := len(*s)
	num1 := (*s)[l-2]
	num2 := (*s)[l-1]
	var res int
	switch op {
	case "+":
		res = num1 + num2
	case "-":
		res = num1 - num2
	case "*":
		res = num1 * num2
	case "/":
		res = num1 / num2
	}
	(*s)[l-2] = res
	*s = (*s)[:l-1]
}

func main() {
	fmt.Println(evalRPN([]string{"2", "1", "+", "3", "*"}))
}