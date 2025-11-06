import math

import numpy as np
from sympy import isprime


class Tabla:
    __M: int
    __arreglo: np.ndarray
    __salto: int

    def __init__(self, n: int):
        self.__M = self.siguiente_primo(n / 0.7)
        self.__arreglo = np.full(self.__M, None)
        self.__salto = 1

    def siguiente_primo(self, numero: float):
        numero = math.ceil(numero)
        while not isprime(numero):
            numero += 1
        return numero

    def hash(self, elemento: int):
        corte = 10 ** len(str(self.__M))
        sum = 0
        while elemento > 0:
            parte = elemento % corte
            sum += parte
            elemento //= corte

        return sum % self.__M

    def insertar(self, elemento: int):
        i = self.hash(elemento)
        while self.__arreglo[i]:
            i = (i + self.__salto) % self.__M
        self.__arreglo[i] = elemento

    def buscar(self, elemento: int):
        i = self.hash(elemento)
        while self.__arreglo[i] and self.__arreglo[i] != elemento:
            print(i)
            i = (i + self.__salto) % self.__M
        return self.__arreglo[i]

    def mostrar(self):
        print(self.__arreglo)


if __name__ == '__main__':
    dnis = [
        41876435, 40346568, 39547821, 42765893, 41234567,
        38456219, 43657842, 40987654, 39876543, 42548976,
    ]
    tabla = Tabla(len(dnis))

    for dni in dnis:
        tabla.insertar(dni)
    tabla.hash(dnis[0])

    tabla.buscar(41234567)

    tabla.mostrar()
