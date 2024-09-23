import numpy as np


class ListaSecuencial:
    __dimension: int
    __ultimo: int
    __cantidad: int
    __items: np.ndarray

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__ultimo = -1
        self.__items = np.empty(dimension, dtype=int)

    def insertar_posicion(self, item, posicion):
        if self.__cantidad == self.__dimension:
            print("Lista llena")
            return None
        if 0 <= posicion < self.__dimension and self.hay_posicion_disponible():
            i = self.__ultimo + 1
            while i > posicion:
                self.__items[i] = self.__items[i - 1]
                i -= 1
            self.__items[i] = item
            self.__cantidad += 1
            self.__ultimo += 1
            return item
        print("Posicion invalida")
        return None

    def insertar_contenido(self, item):
        if self.__cantidad == self.__dimension:
            print("Lista llena")
            return None
        if self.vacia():
            self.__ultimo += 1
            self.__items[self.__ultimo] = item
            self.__cantidad += 1
            return item
        i = 0
        while i <= self.__ultimo and self.__items[i] < item:
            i += 1
        for j in range(self.__ultimo + 1, i, -1):
            self.__items[j] = self.__items[j - 1]
        self.__items[i] = item
        self.__ultimo += 1
        self.__cantidad += 1
        return item

    def suprimir_posicion(self, posicion):
        if self.vacia():
            print("Lista vacia")
            return None
        if 0 <= posicion <= self.__ultimo:
            i = self.__ultimo
            eliminado = self.__items[posicion]
            while i < posicion:
                self.__items[i] = self.__items[i + 1]
                i += 1
            self.__ultimo -= 1
            self.__cantidad -= 1
            return eliminado
        print("Posicion invalida")
        return None

    def suprimir_contenido(self, item):
        if self.vacia():
            print("Lista vacia")
            return None
        i = 0
        while i <= self.__ultimo and self.__items[i] < item:
            i += 1
        if self.__items[i] != item:
            print("Elemento no encontrado")
            return None
        eliminado = self.__items[i]
        for j in range(i, self.__ultimo):
            self.__items[j] = self.__items[j + 1]
        self.__ultimo -= 1
        self.__cantidad -= 1
        return eliminado

    def buscar(self, item):
        if self.vacia():
            print("Lista vacia")
            return None

        i = 0
        while i <= self.__ultimo and self.__Items[i] < item:
            i += 1
        if self.__items[i] == item:
            return i
        print("Elemento no encontrado")
        return None

    def primer_elemento(self):
        if self.vacia():
            print("Lista vacia")
            return None
        return self.__items[0]

    def ultimo_elemento(self):
        if self.vacia():
            print("Lista vacia")
            return None
        return self.__items[self.__ultimo]

    def siguiente(self, posicion):
        if 0 <= posicion <= self.__ultimo:
            if posicion == self.__ultimo:
                print("Ingreso la ultima posicion")
                return None
            return self.__items[posicion + 1]
        print("Posicion invalida")
        return None

    def anterior(self, posicion):
        if 0 <= posicion <= self.__ultimo:
            if posicion == 0:
                print("Ingreso la primera posicion")
                return None
            return self.__items[posicion - 1]
        print("Posicion invalida")
        return None

    def recorrer(self):
        if self.vacia():
            print("Lista vacia")
            return None
        for i in range(self.__ultimo + 1):
            print(self.__items[i], end=" ")
        print()

    def vacia(self):
        return self.__cantidad == 0

    def llena(self):
        return self.__cantidad == self.__dimension
