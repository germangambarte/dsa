package main

import (
	"dsa/internal/stacks"
	"fmt"
)

type Camino struct {
	n        int
	solucion string
}

func buscarCaminos(s *stacks.Secuential[Camino]) {
	for !s.IsEmpty() {
		camino, _ := s.Delete()
		if camino.n == 0 {
			fmt.Println(camino.solucion)
		}
		if camino.n >= 1 {
			s.Insert(Camino{n: camino.n - 1, solucion: camino.solucion + "1"})
		}
		if camino.n >= 2 {
			s.Insert(Camino{n: camino.n - 2, solucion: camino.solucion + "2"})
		}
	}
}

func main() {
	stack := stacks.NewSecuentialStack[Camino](10)
	stack.Insert(Camino{n: 4, solucion: ""})
	buscarCaminos(stack)
}
