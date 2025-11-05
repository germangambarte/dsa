import numpy as np


class Bucket:
    __longitud: int
    __lista: np.ndarray

    def __init__(self, capacidad: int) -> None:
        self.__longitud = 0
        self.__lista = np.empty(capacidad, dtype=object)

    def insertar(self, item: object) -> int | None:
        j = self.__longitud
        while j > 0 and item <= self.__lista[j - 1]:
            self.__lista[j] = self.__lista[j - 1]
            j -= 1
        self.__lista[j] = item
        self.__longitud += 1

    def buscar(self, item: object) -> int | None:
        primero = 0
        ultimo = self.__longitud - 1
        i = None
        while primero <= ultimo and i is None:
            medio = int((primero + ultimo) / 2)
            if item == self.__lista[medio]:
                i = medio
            elif item < self.__lista[medio]:
                ultimo = medio - 1
            else:
                primero = medio + 1
        return i

    def mostrar(self):
        for i in range(self.__longitud):
            print(self.__lista[i], end=", ")
        print()
