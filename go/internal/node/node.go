package node

type Node[T any] struct {
	Item T
	Next *Node[T]
}

func NewNode[T any](item T, node *Node[T]) *Node[T] {
	return &Node[T]{
		Item: item,
		Next: node,
	}
}
