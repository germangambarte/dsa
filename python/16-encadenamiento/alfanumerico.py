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

    def hash(self, elemento: str):
        suma = 0
        i = 1
        for char in elemento:
            if char.isalpha():
                suma += ord(char)
            else:
                suma += int(char)
            i += 1
        return suma % self.__M

    def insertar(self, elemento: str):
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
    patentes = [
        "AB123CD",
        "AC456EF",
        "AD789GH",
        "AE234JK",
        "AF567LM",
        "GHI123",
        "JKL456",
        "MNO789",
        "PRS234",
        "TUV567"
    ]

    tabla = Tabla(len(patentes), 3)

    for patente in patentes:
        tabla.insertar(patente)
    # print(tabla.hash(patentes[1]))

    tabla.buscar("GHI123")

    tabla.mostrar()
