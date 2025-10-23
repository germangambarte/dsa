package queues

import (
	"errors"
	"fmt"
)

type LinkedQueue struct {
	longitud int
	ultimo   *Node
	primero  *Node
}

func NewLinkedQueue(capacidad int) *LinkedQueue {
	return &LinkedQueue{
		longitud: 0,
		ultimo:   nil,
		primero:  nil,
	}
}

func (q *LinkedQueue) Push(item int) {
	newNode := NewNode(item, nil)
	if q.Vacia() {
		q.primero = newNode
	} else {
		q.ultimo.SetNext(newNode)
	}
	q.ultimo = newNode
	q.longitud++
}

func (q *LinkedQueue) Pop() (error, int) {
	if q.Vacia() {
		return errors.New("pila vacia."), -1
	}
	temp := q.primero
	q.primero = q.primero.GetNext()
	q.longitud--
	return nil, temp.GetItem()
}

func (q *LinkedQueue) Travel() {
	actual := q.primero
	for actual != nil {
		fmt.Printf("%d ", actual.GetItem())
		actual = actual.GetNext()
	}
	fmt.Println()
}

func (q *LinkedQueue) Vacia() bool {
	return q.longitud == 0
}
