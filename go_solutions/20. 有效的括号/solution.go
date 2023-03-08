package solution

import (
	"sync"
)

type (
	Stack struct {
		top    *node
		length int
		lock   *sync.RWMutex
	}
	node struct {
		value interface{}
		prev  *node
	}
)

// NewStack Create a new stack
func NewStack() *Stack {
	return &Stack{nil, 0, &sync.RWMutex{}}
}

// Len Return the number of items in the stack
func (s *Stack) Len() int {
	return s.length
}

// Peek View the top item on the stack
func (s *Stack) Peek() interface{} {
	if s.length == 0 {
		return nil
	}
	return s.top.value
}

// Pop the top item of the stack and return it
func (s *Stack) Pop() interface{} {
	s.lock.Lock()
	defer s.lock.Unlock()
	if s.length == 0 {
		return nil
	}
	n := s.top
	s.top = n.prev
	s.length--
	return n.value
}

// Push a value onto the top of the stack
func (s *Stack) Push(value interface{}) {
	s.lock.Lock()
	defer s.lock.Unlock()
	n := &node{value, s.top}
	s.top = n
	s.length++
}

// isValid sa
func isValid(s string) bool {
	stack := NewStack()

	for _, char := range s {
		if string(char) == ")" && stack.Peek().(string) == "(" {
			stack.Pop()
		} else if string(char) == "]" && stack.Peek().(string) == "[" {
			stack.Pop()
		} else if string(char) == "}" && stack.Peek().(string) == "{" {
			stack.Pop()

		} else {
			stack.Push(string(char))
		}
	}
	//for _, char := range "aaaa" {
	//	fmt.Printf("%+v", string(char))
	//}
	if stack.Peek() != nil {
		return false
	}
	return true
}
