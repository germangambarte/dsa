package stacks

import (
	"errors"
	"fmt"
)

type SecuentialStack struct {
	capacity int
	length  int
	last    int
	stack      []int
}

func NewSecuentialStack(capacidad int) *SecuentialStack {
	return &SecuentialStack{
		capacity: capacidad,
		length:  0,
		last:    0,
		stack:      make([]int, capacidad)}
}

func (s *SecuentialStack) Push(item int) error {
	if s.Full() {
		return errors.New("pila llena.")
	}
	s.stack[s.last] = item
	s.last++
	s.length++
	return nil
}

func (s *SecuentialStack) Pop() (error, int) {
	if s.Empty() {
		return errors.New("pila vacia."), -1
	}
	s.last--
	temp := s.stack[s.last]
	s.length--
	return nil, temp
}

func (s *SecuentialStack) Travel() {
	i := s.last - 1
	for i >= 0 {
		fmt.Printf("%d ", s.stack[i])
		i--
	}
	fmt.Println()
}

func (s *SecuentialStack) Full() bool {
	return s.length == s.capacity
}

func (s *SecuentialStack) Empty() bool {
	return s.length == 0
}
