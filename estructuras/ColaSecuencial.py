import numpy as np


class ColaSecuencial:
    __dimension: int
    __cantidad: int
    __ultimo: int
    __primero: int
    __items: np.ndarray

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__ultimo = 0
        self.__primero = 0
        self.__items = np.empty(dimension, dtype=int)

    def insertar(self, item):
        if self.__cantidad == self.__dimension:
            print("Cola llena.")
            return None
        self.__items[self.__ultimo] = item
        self.__ultimo = (self.__ultimo + 1) % self.__dimension
        self.__cantidad += 1
        return item

    def suprimir(self):
        if self.vacia():
            print("Cola vacia.")
            return None
        eliminado = self.__items[self.__primero]
        self.__primero = (self.__primero + 1) % self.__dimension
        self.__cantidad -= 1
        return eliminado

    def recorrer(self):
        if self.vacia():
            print("Cola vacia.")
            return None
        i = self.__primero
        for _ in range(self.__cantidad):
            print(self.__items[i], end=" ")
            i = (i + 1) % self.__dimension
        print("\n")

    def vacia(self):
        return self.__cantidad == 0


if __name__ == "__main__":
    cola = ColaSecuencial(4)

    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)

    cola.recorrer()

    cola.suprimir()
    cola.suprimir()

    cola.recorrer()
