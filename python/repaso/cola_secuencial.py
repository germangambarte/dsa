import numpy as np


class Cola:
    __pri: int
    __ult: int
    __cap: int
    __cola: np.ndarray

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__pri = 0
        self.__ult = 0
        self.__cola = np.empty(cap, dtype=int)

    def insertar(self, item):
        if self.llena():
            print("cola llena.")
            return
        self.__cola[self.__ult] = item
        self.__ult += 1

    def eliminar(self):
        if self.vacia():
            print("cola vacia")
            return
        temp = self.__cola[self.__pri]
        i = self.__pri
        while i < self.__ult - 1:
            self.__cola[i] = self.__cola[i + 1]
            i += 1
        self.__ult-=1
        return temp

    def recorrer(self):
        i = self.__pri
        while i < self.__ult:
            print(self.__cola[i], end=" ")
            i += 1
        print()

    def vacia(self):
        return self.__pri == self.__ult

    def llena(self):
        return self.__ult == self.__cap


if __name__ == "__main__":
    cola = Cola(3)
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)

    cola.recorrer()

    cola.eliminar()

    cola.recorrer()
