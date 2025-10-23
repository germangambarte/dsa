package stacks

type Node struct {
	item int
	next *Node
}

func NewNode(item int, next *Node) *Node {
	return &Node{
		item: item,
		next: next,
	}
}

func (n *Node) GetItem() int {
	return n.item
}
func (n *Node) GetNext() *Node {
	return n.next
}
func (n *Node) SetNext(next *Node) {
	n.next = next
}
