import math

import numpy as np


class Bucket:
    __capacidad: int
    __longitud: int
    __lista: np.ndarray

    def __init__(self, capacidad: int) -> None:
        self.__capacidad = capacidad
        self.__longitud = 0
        self.__lista = np.empty(capacidad, dtype=object)

    def insertar(self, item: object) -> int | None:
        if self.llena():
            print("lista llena.")
            return None

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

    def llena(self):
        return self.__longitud == self.__capacidad

    def vacia(self):
        return self.__longitud == 0


class Tabla:
    __M: int
    __T: int
    __N: int
    __D: int
    __arreglo: np.ndarray
    __area_overflow: int

    def __init__(self, n: int, d: int) -> None:
        self.__M = int((n / d))
        self.__T = math.ceil(self.__M * 1.2)
        self.__D = d
        self.__arreglo = np.empty(self.__T, dtype=Bucket)
        self.__area_overflow = int(self.__T - math.ceil(self.__M * 0.2))
        print(f"M: {self.__M}")
        print(f"T: {self.__T}")
        print(f"D: {self.__D}")
        print(f"overflow: {self.__area_overflow}")

    def hash(self, valor):
        return valor % self.__M

    def insertar(self, item):
        dir = self.hash(item)
        if self.__arreglo[dir] is None:
            self.__arreglo[dir] = Bucket(self.__D)

        if self.__arreglo[dir].llena():
            dir = self.__area_overflow
            hay_espacio = False
            while dir < self.__T and not hay_espacio:
                if self.__arreglo[dir] is None:
                    self.__arreglo[dir] = Bucket(self.__D)

                if self.__arreglo[dir].llena():
                    dir += 1
                else:
                    hay_espacio = True

            if not hay_espacio:
                print(f"No hay espacio para insertar el item: {item}")
                return
        self.__arreglo[dir].insertar(item)

    def buscar(self, item):
        dir = self.hash(item)

        if self.__arreglo[dir] is None:
            return None

        resultado = self.__arreglo[dir].buscar(item)
        if resultado is not None:
            return resultado

        encontrado = False
        if self.__arreglo[dir].llena():
            dir = self.__area_overflow
            while dir < self.__T and not encontrado:
                if self.__arreglo[dir]:
                    resultado = self.__arreglo[dir].buscar(item)
                    if resultado is None:
                        dir += 1
                    else:
                        encontrado = True

        return resultado

    def mostrar(self):
        dir = 0
        while dir < self.__T:
            if self.__arreglo[dir]:
                print(f"[{dir}]:", end=" ")
                self.__arreglo[dir].mostrar()
            else:
                print(f"[{dir}]: None")
            dir += 1


if __name__ == "__main__":
    items = [1, 5, 6, 4, 7, 9, 3, 46, 75, 14, 27]
    tabla = Tabla(12, 4)

    for item in items:
        tabla.insertar(item)
    tabla.mostrar()
    print(tabla.buscar(14))
    print(tabla.buscar(27))
    print(tabla.buscar(11))
