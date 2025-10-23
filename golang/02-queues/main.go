package main

import "queues/queues"

func main(){
	// queue := queues.NewSecuentialQueue(3)
	queue := queues.NewLinkedQueue(3)

	queue.Push(1)
	queue.Push(2)
	queue.Push(3)
	queue.Push(4)

	queue.Travel()

	queue.Pop()

	queue.Travel()
}

