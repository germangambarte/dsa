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

    def hash(self, patente: str):
        sum = 0
        i = 1

        for letra in patente:
            if letra.isalpha():
                sum += ord(letra) * (10 ** i)
            else:
                sum += int(letra) * (10 ** i)
            i += 1
        print(sum)

        return sum % self.__M

    def insertar(self, patente: str):
        i = self.hash(patente)
        while self.__arreglo[i]:
            i = (i + self.__salto) % self.__M
        self.__arreglo[i] = patente

    def buscar(self, patente: str):
        i = self.hash(patente)
        while self.__arreglo[i] and self.__arreglo[i] != patente:
            i = (i + self.__salto) % self.__M
        return self.__arreglo[i]

    def mostrar(self):
        print(self.__arreglo)


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

    tabla = Tabla(len(patentes))

    for patente in patentes:
        tabla.insertar(patente)
    # print(tabla.hash(patentes[1]))

    tabla.buscar("GHI123")

    tabla.mostrar()
