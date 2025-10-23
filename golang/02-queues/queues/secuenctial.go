package queues

import (
	"errors"
	"fmt"
)

type SecuentialQueue struct {
	capacidad int
	longitud  int
	ultimo    int
	primero   int
	cola      []int
}

func NewSecuentialQueue(capacidad int) *LinkedQueue {
	return &LinkedQueue{
		capacidad: capacidad,
		longitud:  0,
		ultimo:    0,
		primero:   0,
		cola:      make([]int, capacidad),
	}
}

func (s *LinkedQueue) Push(item int) error {
	if s.Llena() {
		return errors.New("pila llena.")
	}
	s.cola[s.ultimo] = item
	s.ultimo++
	s.longitud++
	return nil
}

func (s *LinkedQueue) Pop() (error, int) {
	if s.Vacia() {
		return errors.New("pila vacia."), -1
	}
	temp := s.cola[s.primero]
	i := s.primero
	for i < s.ultimo-1 {
		s.cola[i] = s.cola[i+1]
		i++
	}
	s.ultimo--
	s.longitud--
	return nil, temp
}

func (q *LinkedQueue) Travel() {
	i := q.primero
	for i < q.ultimo {
		fmt.Printf("%d ", q.cola[i])
		i++
	}
	fmt.Println()
}

func (q *LinkedQueue) Llena() bool {
	return q.longitud == q.capacidad
}

func (q *LinkedQueue) Vacia() bool {
	return q.longitud == 0
}
