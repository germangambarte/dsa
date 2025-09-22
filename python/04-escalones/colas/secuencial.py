import numpy as np


class Cola_Secuencial:
    __cola: np.ndarray
    __primero: int
    __ultimo: int
    __cantidad: int
    __tamaño: int

    def __init__(self, tamaño) -> None:
        self.__tamaño = tamaño
        self.__primero = 0
        self.__ultimo = 0
        self.__cantidad = 0
        self.__cola = np.zeros(self.__tamaño, dtype=object)

    def insertar(self, item):
        if self.llena():
            print("cola llena.")
            return
        self.__cola[self.__ultimo] = item
        self.__ultimo = (self.__ultimo + 1) % self.__tamaño
        self.__cantidad += 1

    def eliminar(self):
        if self.vacia():
            print("pila vacia.")
            return
        temp = self.__cola[self.__primero]
        self.__primero = (self.__primero + 1) % self.__tamaño
        self.__cantidad -= 1
        return temp

    def mostrar(self):
        if self.vacia():
            print("pila vacia.")

        i = self.__primero
        j = 0
        while j < self.__cantidad:
            print(self.__cola[i])
            i = (i + 1) % self.__tamaño
            j += 1

    def vacia(self):
        return self.__cantidad == 0

    def llena(self):
        return self.__cantidad == self.__tamaño

    def obtener_cantidad(self):
        return self.__cantidad


if __name__ == "__main__":
    cola = Cola_Secuencial(3)

    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)

    cola.mostrar()
