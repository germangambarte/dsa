package main

import (
	"dsa/internal/stacks"
	"errors"
	"fmt"
	"math"
)

type Hanoi struct {
	towers           []*stacks.Linked[int]
	movements        int
	minimumMovements int
}

func NewHanoi(n int) *Hanoi {
	initializedTower := stacks.NewLinkedStack[int]()

	for i := n; i > 0; i-- {
		initializedTower.Insert(i)
	}

	return &Hanoi{
		towers: []*stacks.Linked[int]{
			stacks.NewLinkedStack[int](),
			stacks.NewLinkedStack[int](),
			initializedTower,
		},
		movements:        0,
		minimumMovements: int(math.Pow(2, float64(n))) - 1,
	}
}

func (h *Hanoi) tryMove(originDiskNumber, destinationDiskNumber int) error {
	fmt.Println(originDiskNumber, destinationDiskNumber)
	if 0 > originDiskNumber || originDiskNumber > 2 || 0 > destinationDiskNumber || destinationDiskNumber > 2 {
		return errors.New("Número de disco no válido")
	}
	originTower := h.towers[originDiskNumber]

	if originTower.IsEmpty() {
		return errors.New("la pila origen está vacia")
	}

	originDisk, _ := originTower.Delete()
	destinationTower := h.towers[destinationDiskNumber]

	if destinationTower.IsEmpty() {
		destinationTower.Insert(originDisk)
		h.movements++
		return nil
	}

	destinationDisk, _ := destinationTower.Delete()

	if originDisk > destinationDisk {
		destinationTower.Insert(destinationDisk)
		originTower.Insert(originDisk)
		return fmt.Errorf("moviemiento no válido. disco %d > disco %d", originDisk, destinationDisk)
	}

	destinationTower.Insert(destinationDisk)
	destinationTower.Insert(originDisk)
	h.movements++
	return nil
}

func (h *Hanoi) checkWin() bool {
	return h.towers[1].IsEmpty() && h.towers[2].IsEmpty()
}

func (h *Hanoi) mostrar() {
	for i, v := range h.towers {
		fmt.Printf("[%d] ", i+1)
		v.Show()
	}
}

func main() {
	game := NewHanoi(3)
	var originTowerNumber int
	game.mostrar()
	fmt.Print("Elija una torre: ")
	fmt.Scan(&originTowerNumber)

	for originTowerNumber != 0 {
		var destinationTowerNumber int
		fmt.Print("Elija otra torre: ")
		fmt.Scan(&destinationTowerNumber)

		err := game.tryMove(originTowerNumber-1, destinationTowerNumber-1)
		if err != nil {
			fmt.Println(err.Error())
		}

		fmt.Println()
		game.mostrar()
		fmt.Println()

		if game.checkWin() {
			fmt.Println("Juego terminado.")
			fmt.Printf("Cantidad de movimientos realizados: %d\n", game.movements)
			fmt.Printf("Cantidad de movimientos mínimos: %d\n", game.minimumMovements)
			originTowerNumber = 0
		} else {
			fmt.Print("Elija una torre: ")
			fmt.Scan(&originTowerNumber)
		}
	}
}
