package main

import (
	"stack/stacks"
)

func main() {
	// stack := stacks.NewSecuentialStack(3)
	stack := stacks.NewLinkedStack()

	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
 	stack.Push(4)
	stack.Travel()
	stack.Pop()
	stack.Travel()
}
