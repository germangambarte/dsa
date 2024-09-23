from typing import Optional

import numpy as np


class Nodo:
    __item: int
    __siguiente: Optional[int]

    def __init__(self, siguiente=None):
        self.__item = 0
        self.__siguiente = siguiente

    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente


class Lista:
    __maximo: int
    __cabeza: int
    __cantidad: int
    __espacio: np.ndarray
    __disponible: int

    def __init__(self, max=0):
        self.__maximo = max
        self.__cabeza = 0
        self.__cantidad = 0
        self.__disponible = 0
        self.__espacio = np.empty(shape=max, dtype=Nodo)
        for i in range(self.__maximo):
            self.__espacio[i] = Nodo()

    def vacia(self):
        return self.__cantidad == 0

    def get_disponible(self):
        i = 0
        while i < self.__maximo and self.__espacio[i].get_siguiente() is not None:
            i += 1
        if i < self.__maximo:
            self.__disponible = i
            # print(f"disponible: {self.__disponible}")
            return True
        else:
            self.__disponible = -1
            return False

    def liberar_disponible(self, disp: int):
        if disp >= 0 and disp < self.__maximo:
            self.__espacio[disp].set_siguiente(None)
            return True
        else:
            return False

    def insertar(self, item: int, posicion: int):
        if (
            self.__cantidad < self.__maximo
            and posicion >= 0
            and posicion <= self.__cantidad
            and self.get_disponible()
        ):

            self.__espacio[self.__disponible].set_item(item)
            anterior = self.__cabeza
            cabeza = self.__cabeza
            i = 0
            while i < posicion:
                i += 1
                anterior = cabeza
                cabeza = self.__espacio[cabeza].get_siguiente()
            print(f"posicion: {posicion}, i: {i}")

            if cabeza == self.__cabeza:
                if self.vacia():
                    self.__espacio[self.__cabeza].set_siguiente(None)
                else:
                    self.__espacio[self.__disponible].set_siguiente(self.__cabeza)
                    self.__cabeza = self.__disponible
            elif cabeza is None:
                self.__espacio[self.__disponible].set_siguiente(None)
                self.__espacio[anterior].set_siguiente(self.__disponible)
            else:
                self.__espacio[self.__disponible].set_siguiente(cabeza)
                self.__espacio[anterior].set_siguiente(self.__disponible)
            self.__cantidad += 1
            return True
        else:
            print("Espacio lleno")
            return False

    def recorrer(self):
        if self.vacia():
            print("Lista vacia.")
            return None
        else:
            cabeza = self.__cabeza
            i = 0
            while i < self.__cantidad and cabeza < self.__maximo:
                print(self.__espacio[cabeza].get_item(), end=" ")
                cabeza = self.__espacio[cabeza].get_siguiente()
                i += 1
            print("\n")
            return True


if __name__ == "__main__":
    lista = Lista(5)
    lista.insertar(1, 0)
    lista.insertar(2, 1)
    lista.insertar(3, 0)
    lista.insertar(4, 2)
    lista.insertar(5, 1)
    lista.recorrer()
