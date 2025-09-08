package queues

import (
	"errors"
	"fmt"
)

type Secuential struct {
	length   int
	capacity int
	last     int
	first    int
	queue    []int
}

func NewSecuentialQueue(capacity int) *Secuential {
	return &Secuential{
		capacity: capacity,
		length:   0,
		last:     0,
		first:    0,
		queue:    make([]int, capacity),
	}
}

func (s *Secuential) Insert(item int) error {
	if s.isFull() {
		return errors.New("cola llena")
	}
	s.queue[s.last] = item
	s.last = (s.last + 1) % s.capacity
	s.length++
	return nil
}

func (s *Secuential) Delete() (int, error) {
	if s.isEmpty() {
		return 0, errors.New("cola vacia")
	}
	temp := s.queue[s.first]
	s.first = (s.first + 1) % s.capacity
	s.length--
	return temp, nil
}

func (s *Secuential) Show() {
	for i, j := s.first, 0; j < s.length; i, j = (i+1)%s.capacity, j+1 {
		fmt.Printf("%d ", s.queue[i])
	}
	fmt.Println()
}

func (s *Secuential) isEmpty() bool {
	return s.length == 0
}

func (s *Secuential) isFull() bool {
	return s.length == s.capacity
}
