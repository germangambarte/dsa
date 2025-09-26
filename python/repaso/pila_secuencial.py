import numpy as np


class Pila:
    __cap: int
    __long: int
    __pila: np.ndarray

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__long = 0
        self.__pila = np.empty(cap, dtype=int)

    def insertar(self, item):
        if self.llena():
            print("pila llena.")
            return
        self.__pila[self.__long] = item
        self.__long += 1

    def suprimir(self):
        if self.vacia():
            print("Pila vacia.")
            return
        self.__long -= 1
        return self.__pila[self.__long]

    def recorrer(self):
        i = 0
        while i < self.__long:
            print(self.__pila[i], end=" ")
            i += 1
        print()

    def vacia(self):
        return self.__long == 0

    def llena(self):
        return self.__long == self.__cap


if __name__ == "__main__":
    pila = Pila(3)
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)

    pila.recorrer()

    pila.suprimir()

    pila.recorrer()
