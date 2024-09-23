import numpy as np
import pdb


class Lista:
    __dimension: int
    __ultimo: int
    __arreglo: np.ndarray
    __cantidad: int

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__ultimo = -1
        self.__cantidad = 0
        self.__arreglo = np.empty(dimension, dtype="int")

    def insertar_por_posicion(self, item, posicion):
        if not self.llena():
            if posicion >= 0 and posicion <= self.__ultimo + 1:
                i = self.__ultimo + 1
                while i > posicion:
                    self.__arreglo[i] = self.__arreglo[i - 1]
                    i -= 1
                self.__arreglo[i] = item
                self.__cantidad += 1
                self.__ultimo += 1
            else:
                print("Posicion no valida.")
        else:
            print("Arreglo lleno.")

    def insertar_por_contenido(self, item):
        pdb.set_trace()
        if not self.llena():
            if self.vacia():
                self.__ultimo += 1
                self.__arreglo[self.__ultimo] = item
                self.__cantidad += 1
            else:
                i = 0
                while self.__arreglo[i] < item and i <= self.__ultimo:
                    i += 1
                for j in range(self.__ultimo + 1, i, -1):
                    self.__arreglo[j] = self.__arreglo[j - 1]
                self.__arreglo[i] = item
                self.__cantidad += 1
                self.__ultimo += 1
        else:
            print("Arreglo lleno.")

    def suprimir_por_contenido(self, item):
        if self.vacia():
            print("Lista vacia.")
        else:
            i = 0
            while i <= self.__ultimo and self.__arreglo[i] != item:
                i += 1
            for j in range(i, self.__ultimo):
                self.__arreglo[j] = self.__arreglo[j + 1]
            self.__ultimo -= 1
            self.__cantidad -= 1

    def suprimir_por_posicion(self, posicion):
        if self.vacia():
            print("Lista vacia.")
        else:
            if posicion >= 0 and posicion <= self.__ultimo:
                i = self.__ultimo
                eliminado = self.__arreglo[posicion]
                while posicion < i:
                    self.__arreglo[posicion] = self.__arreglo[posicion + 1]
                    posicion += 1
                self.__ultimo -= 1
                self.__cantidad -= 1
                return eliminado

    def buscar(self, item):
        if self.vacia():
            print("Lista vacia")
            return None
        i = 0
        while i <= self.__ultimo and self.__arreglo[i] != item:
            i += 1
        if self.__arreglo[i] == item:
            return i
        else:
            return None

    def primer_elemento(self):
        return self.__arreglo[0]

    def ultimo_elemento(self):
        return self.__arreglo[self.__ultimo]

    def siguiente(self, posicion):
        if self.vacia():
            print("Lista vacia.")
            return None
        if posicion >= 0 and posicion <= self.__ultimo:
            if posicion == self.__ultimo:
                print("Ingreso la ultima posicion, no hay siguiente")
                return None
            else:
                return self.__arreglo[posicion + 1]
        else:
            print("Posicion no valido.")
            return None

    def anterior(self, posicion):
        if self.vacia():
            print("Lista vacia.")
            return None
        if posicion >= 0 and posicion <= self.__ultimo:
            if posicion == 0:
                print("Ingreso la primera posicion, no hay posicion anterior")
                return None
            else:
                return self.__arreglo[posicion - 1]
        else:
            print("Posicion no valida.")
            return None

    def recorrer(self):
        for i in range(self.__cantidad):
            print(self.__arreglo[i], end=" ")
        print("\n")

    def vacia(self):
        return self.__cantidad == 0

    def llena(self):
        return self.__cantidad == self.__dimension


if __name__ == "__main__":
    lista = Lista(5)
    # ---- insertar_por_posicion ----
    # lista.insertar_por_posicion(1, 0)
    # lista.insertar_por_posicion(2, 1)
    # lista.insertar_por_posicion(3, 0)
    # lista.insertar_por_posicion(4, 2)
    # lista.insertar_por_posicion(5, 1)
    # lista.recorrer()
    # ---- insertar_por_contenido ----
    lista.insertar_por_contenido(3)
    lista.insertar_por_contenido(5)
    lista.insertar_por_contenido(1)
    lista.insertar_por_contenido(4)
    lista.insertar_por_contenido(2)
    lista.recorrer()
    # ---- suprimir_por_contenido ----
    # lista.suprimir_por_contenido(2)
    # lista.recorrer()
    # ---- suprimir_por_posicion ----
    # lista.suprimir_por_posicion(2)
    # lista.recorrer()
