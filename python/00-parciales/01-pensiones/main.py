import random
import numpy as np
# Ejercicio 2: encontrar TAD adecuado
# - simular durante 5 horas
# - dos cajeros
# - tiempo de atención: 6 y 4 minutos
# - frecuencia de llegada de pensionados: 3 minutos

class Nodo:
    def __init__(self, item: int, sig=None) -> None:
        self.__item = item
        self.__sig = sig

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__sig

    def set_siguiente(self, sig: "Nodo"):
        self.__sig = sig


class Cola:
    __cabeza: Nodo | None
    __cola: Nodo | None
    __cantidad: int

    def insertar(self, item):
        nuevo_nodo = Nodo(item)
        if self.__cantidad == 0:
            self.__cabeza = nuevo_nodo
        else :
            self.__cola.set_siguiente(nuevo_nodo)
        self.__cola = nuevo_nodo
        self.__cantidad += 1

    def eliminar(self):
        pass

    def recorrer(self):
        pass

    def vacia(self):
        pass


class Cajero(Cola):
    __tiempo_de_atencion: int

    def __init__(self, tiempo_de_atencion: int) -> None:
        super().__init__()
        self.__tiempo_de_atencion = tiempo_de_atencion


def algoritmo():
    cajeros = np.array([Cajero(6), Cajero(4)])
    cajero = random.randint(0, 1)
    for tiempo in range(300):
        if tiempo % 3 == 0:
            cajeros[cajero].insertar(1)
            cajero = random.randint(0, 1)
        if tiempo % 4 == 0:
            cajeros[1].eliminar()
        if tiempo % 6 == 0:
            cajeros[0].eliminar()
