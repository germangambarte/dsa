package queues

import (
	"errors"
	"fmt"
	"dsa/internal/node"
)

type Linked[T any] struct {
	head   *node.Node[T]
	tail   *node.Node[T]
	length int
}

func NewLinkedQueue[T any]() *Linked[T] {
	return &Linked[T]{
		head:   nil,
		tail:   nil,
		length: 0,
	}
}

func (q *Linked[T]) Insert(item T) {
	newNode := node.NewNode(item, nil)
	if q.isEmpty() {
		q.head = newNode
	} else {
		q.tail.Next = newNode
	}
	q.tail = newNode
	q.length++
}

func (q *Linked[T]) Delete() (T, error) {
	if q.isEmpty() {
		var zero T
		return zero, errors.New("cola vacia")
	}
	temp := q.head
	q.head = q.head.Next
	q.length--
	return temp.Item, nil
}

func (q *Linked[T]) Show() {
	current := q.head
	for current != nil {
		fmt.Printf("%v ", current.Item)
		current = current.Next
	}
	fmt.Println()
}

func (q *Linked[T]) isEmpty() bool {
	return q.length == 0
}
