import numpy as np


class Pila:
    __pila: np.ndarray
    __capacidad: int
    __longitud: int

    def __init__(self, capacidad) -> None:
        self.__capacidad = capacidad
        self.__longitud = 0
        self.__pila = np.empty(capacidad,dtype=int)

    def insertar(self, item):
        if self.llena():
            print("pila llena.")
            return None
        self.__pila[self.__longitud] = item
        self.__longitud += 1

    def eliminar(self):
        pass

    def recorrer(self):
        i = self.__longitud - 1
        while i >= 0:
            print(self.__pila[i], end=" ")
            i -=1
        print()

    def vacia(self):
        return self.__longitud == 0

    def llena(self):
        return self.__longitud == self.__capacidad


def convertir(pila: Pila, n):
    if n < 2:
        pila.insertar(n)
        return
    pila.insertar(n % 2)
    convertir(pila, int(n / 2))


def convertir_loop(pila, n):
    while n > 1:
        pila.insertar(n % 2)
        n = int(n / 2)
    pila.insertar(n)


if __name__ == "__main__":
    pila1 = Pila(10)
    pila2 = Pila(10)
    convertir(pila1, 100)
    convertir_loop(pila2, 100)

    pila1.recorrer()
    pila2.recorrer()
