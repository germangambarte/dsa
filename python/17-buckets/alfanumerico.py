import math
import numpy as np
from sympy import isprime
from bucket import Bucket


class Tabla:
    __T: int
    __M: int
    __N: int
    __C: int
    __arreglo: np.ndarray
    __contadores: np.ndarray
    __contadores: np.ndarray

    def __init__(self, n: int, c: int):
        self.__N = n
        self.__C = c
        self.__M = math.ceil(n / c)
        self.__T = math.ceil(self.__M * 1.2)
        self.__inicio_overflow = self.__M
        self.__arreglo = np.empty(self.__T, dtype=object)
        self.__contadores = np.zeros(self.__T)
        self.inicializar()

    def inicializar(self):
        for i in range(self.__T):
            self.__arreglo[i] = Bucket(self.__C)

    def siguiente_primo(self, numero: float):
        numero = math.ceil(numero)
        while not isprime(numero):
            numero += 1
        return numero

    def hash(self, elemento: str):
        suma = 0
        i = 0
        for letra in elemento:
            valor = ord(letra) * i if letra.isalpha() else int(letra) * 1
            suma += valor
            i += 1
        return suma % self.__M

    def insertar(self, elemento: str):
        i = self.hash(elemento)

        if self.__contadores[i] < self.__C:
            self.__arreglo[i].insertar(elemento)
            self.__contadores[i] += 1
        else:
            self.insertar_overflow(elemento)

    def insertar_overflow(self, elemento: int):
        i = self.__inicio_overflow
        while self.__contadores[i] == self.__C:
            i += 1
        self.__arreglo[i].insertar(elemento)
        self.__contadores[i] += 1

    def buscar(self, elemento: int):
        i = self.hash(elemento)
        resultado = self.__arreglo[i].buscar(elemento)
        if resultado is None and self.__contadores[i] == self.__C:
            return self.buscar_overflow(elemento)
        else:
            return resultado

    def buscar_overflow(self, elemento: int):
        i = self.__inicio_overflow

        while self.__contadores[i] > 0 and self.__arreglo[i].buscar(elemento) is None:
            i += 1
        return self.__arreglo[i].buscar(elemento)

    def mostrar(self):
        for i in range(self.__T):
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
