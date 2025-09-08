package stacks

import (
	"dsa/internal/node"
	"errors"
	"fmt"
)

type Linked[T any] struct {
	tail   *node.Node[T]
	length int
}

func NewLinkedStack[T any]() *Linked[T] {
	return &Linked[T]{
		tail:   nil,
		length: 0,
	}
}

func (q *Linked[T]) Insert(item T) {
	newNode := node.NewNode(item, q.tail)
	q.tail = newNode
	q.length++
}

func (q *Linked[T]) Delete() (T, error) {
	if q.IsEmpty() {
		var zero T
		return zero, errors.New("cola vacia")
	}
	temp := q.tail
	q.tail = q.tail.Next
	q.length--
	return temp.Item, nil
}

func (q *Linked[T]) Show() {
	current := q.tail
	for current != nil {
		fmt.Printf("%v ", current.Item)
		current = current.Next
	}
	fmt.Println()
}

func (q *Linked[T]) IsEmpty() bool {
	return q.length == 0
}
