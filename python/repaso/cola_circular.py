import numpy as np


class Cola:
    __pri: int
    __ult: int
    __cap: int
    __long: int
    __cola: np.ndarray

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__pri = 0
        self.__ult = 0
        self.__long = 0
        self.__cola = np.empty(cap, dtype=int)

    def insertar(self, item):
        if self.llena():
            print("cola llena")
            return
        self.__cola[self.__ult] = item
        self.__ult = (self.__ult + 1) % self.__cap
        self.__long += 1

    def eliminar(self):
        if self.vacia():
            print("cola vacia.")
            return
        temp = self.__cola[self.__pri]
        self.__pri = (self.__pri + 1) % self.__cap
        self.__long -= 1
        return temp

    def recorrer(self):
        i = self.__pri
        j = 0
        while j < self.__long:
            print(self.__cola[i], end=" ")
            i = (i + 1) % self.__cap
            j += 1
        print()

    def vacia(self):
        return self.__pri == self.__long

    def llena(self):
        return self.__long == self.__cap


if __name__ == "__main__":
    cola = Cola(3)
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)

    cola.recorrer()

    cola.eliminar()

    cola.recorrer()
