import math
import numpy as np
from sympy import isprime
from lista import Lista


class Tabla:
    __M: int
    __N: int
    __C: int
    __arreglo: np.ndarray

    def __init__(self, n: int, c: int):
        self.__N = n
        self.__C = c
        self.__M = self.siguiente_primo(n / c)
        self.__arreglo = np.empty(self.__M, dtype=object)
        self.inicializar()

    def inicializar(self):
        for i in range(self.__M):
            self.__arreglo[i] = Lista()

    def siguiente_primo(self, numero: float):
        numero = math.ceil(numero)
        while not isprime(numero):
            numero += 1
        return numero

    def hash(self, elemento: int):
        return elemento % self.__M

    def insertar(self, elemento: int):
        i = self.hash(elemento)
        self.__arreglo[i].insertar(elemento)

    def buscar(self, elemento: int):
        i = self.hash(elemento)
        return self.__arreglo[i].buscar(elemento)

    def mostrar(self):
        for i in range(self.__M):
            print(f"[{i}]", end=" ")
            self.__arreglo[i].mostrar()


if __name__ == '__main__':
    dnis = [
        41876435, 40346568, 39547821, 42765893, 41234567,
        38456219, 43657842, 40987654, 39876543, 42548976,
    ]
    tabla = Tabla(len(dnis), 3)

    for dni in dnis:
        tabla.insertar(dni)

    print(tabla.buscar(42765893))

    tabla.mostrar()
