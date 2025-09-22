import numpy as np


class Pila_Secuencial:
    __lugar_disponible: int
    __capacidad: int
    __pila: np.ndarray

    def __init__(self, capacidad, pila=None):
        self.__capacidad = capacidad
        if pila is None:
            self.__pila = np.zeros(capacidad, dtype=object)
            self.__lugar_disponible = 0
        else:
            self.__pila = pila
            self.__lugar_disponible = len(pila)

    def insertar(self, item):
        if self.__lugar_disponible == self.__capacidad:
            print("pila llena.")
            return
        self.__pila[self.__lugar_disponible] = item
        self.__lugar_disponible += 1

    def eliminar(self):
        if self.vacia():
            print("pila vacia.")
            return
        temp = self.__pila[self.__lugar_disponible - 1]
        self.__lugar_disponible -= 1

        return temp

    def vacia(self):
        return self.__lugar_disponible == 0

    def mostrar(self):
        if self.vacia():
            print("pila vacia.")
            return

        i = self.__lugar_disponible - 1
        while i >= 0:
            print(self.__pila[i])
            i -= 1

    def longitud(self):
        return self.__lugar_disponible

    def get_pila(self):
        return self.__pila


if __name__ == "__main__":
    pila = Pila_Secuencial(3)
    print("Agregando:")

    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)

    pila.insertar(4)
    pila.mostrar()

    print("Eliminando:")
    print(pila.eliminar())
    print(pila.eliminar())
    print(pila.eliminar())

    print(pila.eliminar())

    pila.mostrar()
