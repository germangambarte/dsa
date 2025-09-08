package stacks

import (
	"errors"
	"fmt"
)

type Secuential[T any] struct {
	length   int
	capacity int
	last     int
	stack    []T
}

func NewSecuentialStack[T any](capacity int) *Secuential[T] {
	return &Secuential[T]{
		capacity: capacity,
		length:   0,
		last:     0,
		stack:    make([]T, capacity),
	}
}

func (s *Secuential[T]) Insert(item T) error {
	if s.isFull() {
		return errors.New("pila llena")
	}
	s.stack[s.last] = item
	s.last++
	s.length++
	return nil
}

func (s *Secuential[T]) Delete() (T, error) {
	if s.IsEmpty() {
		var zero T
		return zero, errors.New("cola vacia")
	}
	s.last--
	temp := s.stack[s.last]
	s.length--
	return temp, nil
}

func (s *Secuential[T]) Show() {
	for i := s.last - 1; i >= 0; i-- {
		fmt.Printf("%v ", s.stack[i])
	}
	fmt.Println()
}

func (s *Secuential[T]) IsEmpty() bool {
	return s.length == 0
}

func (s *Secuential[T]) isFull() bool {
	return s.length == s.capacity
}
