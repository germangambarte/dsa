package stacks

import (
	"errors"
	"fmt"
)

type LinkedStack struct {
	length int
	last   *Node
}

func NewLinkedStack() *LinkedStack {
	return &LinkedStack{
		length: 0,
		last:   nil,
	}
}

func (s *LinkedStack) Push(item int) {
	s.last = NewNode(item, s.last)
	s.length++
}

func (s *LinkedStack) Pop() (error, int) {
	if s.Empty() {
		return errors.New("pila vacia."), -1
	}
	temp := s.last
	s.last = s.last.GetNext()
	s.length--
	return nil, temp.GetItem()
}

func (s *LinkedStack) Travel() {
	current := s.last
	for current != nil{
		fmt.Printf("%d ", current.GetItem())
		current = current.GetNext()
	}
	fmt.Println()
}

func (s *LinkedStack) Empty() bool {
	return s.length == 0
}
