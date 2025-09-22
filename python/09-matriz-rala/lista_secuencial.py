import numpy as np


class Lista:
    __filas: int
    __columnas: int
    __longitud: int
    __lista: np.ndarray

    def __init__(self, filas: int, columnas: int) -> None:
        self.__filas = filas
        self.__columnas = columnas
        self.__longitud = 0
        self.__lista = np.empty((self.__filas, self.__columnas), dtype=int)

    def insertar(self, fila: int, columna: int, item: object) -> int | None:
        if self.llena():
            print("lista llena.")
            return None

        if 1 > fila or fila > self.__filas or 1 > columna or columna > self.__columnas:
            print("posición no válida.")
            return None

        self.__lista[fila - 1][columna - 1] = item
        self.__longitud += 1

    def eliminar(self, fila: int, columna: int) -> int | None:
        if self.vacia():
            print("lista vacia.")
            return None

        if 1 > fila or fila > self.__filas or 1 > columna or columna > self.__columnas:
            print("posición no válida.")
            return None

        temp = self.__lista[fila - 1][columna - 1]
        self.__longitud -= 1

        return temp

    def recuperar(self, fila: int, columna: int) -> int | None:
        if 1 > fila or fila > self.__filas or 1 > columna or columna > self.__columnas:
            print("posición no válida.")
            return None

        return self.__lista[fila - 1][columna - 1]

    def recorrer(self):
        for i in range(self.__filas):
            for j in range(self.__columnas):
                print(self.__lista[i][j], end=" ")
            print()
        print()

    def vacia(self):
        return self.__longitud == 0

    def llena(self):
        return self.__longitud == self.__filas * self.__columnas

    def get_filas(self):
        return self.__filas

    def get_columnas(self):
        return self.__columnas
