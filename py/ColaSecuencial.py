import numpy as np


class ColaSecuencial:
    __items: np.ndarray
    __cantidad: int
    __ultimo: int
    __primero: int
    __dimension: int

    def __init__(self, dim=0) -> None:
        self.__dimension = dim
        self.__items = np.empty(dim)
        self.__cantidad = 0
        self.__ultimo = 0
        self.__primero = 0

    def insertar(self, item: int) -> int:
        if self.__cantidad < self.__dimension:
            self.__items[self.__ultimo] = item
            self.__ultimo = (self.__ultimo + 1) % self.__dimension
            self.__cantidad += 1
            return item
        else:
            print("Pila llena.\n")
            return 0

    def suprimir(self) -> int:
        if self.vacio():
            print("Pila vacia.\n")
            return 0
        else:
            eliminado = self.__items[self.__primero]
            self.__primero = (self.__primero + 1) % self.__dimension
            self.__cantidad -= 1
            return eliminado

    def recorrer(self):
        i = self.__primero
        for _ in range(self.__cantidad):
            print(int(self.__items[i]), end=" ")
            i = (i + 1) % self.__dimension
        print("\n")

    def vacio(self) -> bool:
        return self.__cantidad == 0


if __name__ == "__main__":
    pila = ColaSecuencial(4)

    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)

    pila.recorrer()

    pila.suprimir()
    pila.suprimir()

    pila.recorrer()
