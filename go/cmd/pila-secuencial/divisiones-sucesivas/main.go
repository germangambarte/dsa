package main

import (
	"dsa/internal/stacks"
)

func successiveDivisions(s *stacks.Secuential[int], n int) {
	if n < 2 {
		s.Insert(n)
		return
	}
	s.Insert(n % 2)
	successiveDivisions(s, n/2)
}

func main() {
	stack := stacks.NewSecuentialStack[int](20)
	successiveDivisions(stack, 100)
	stack.Show()
}
