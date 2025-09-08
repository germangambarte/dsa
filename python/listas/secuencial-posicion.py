import numpy as np


class ListaSecuencial:
    __capacidad: int
    __longitud: int
    __lista: np.ndarray

    def __init__(self, capacidad: int) -> None:
        self.__capacidad = capacidad
        self.__longitud = 0
        self.__lista = np.empty(shape=3, dtype=object)

    def insertar(self, posicion: int, item: object) -> int | None:
        if self.llena():
            print("lista llena.")
            return None

        if 1 > posicion > self.__longitud:
            print("posición no válida.")
            return None

        posicion -= 1

        j = self.__longitud
        while posicion != j:
            self.__lista[j] = self.__lista[j - 1]
            j -= 1
        self.__lista[posicion] = item

        self.__longitud += 1

    def eliminar(self, posicion: int) -> object | None:
        if self.vacia():
            print("lista vacia.")
            return None
        if 1 > posicion > self.__longitud:
            print("posición no válida.")
            return None
        posicion -= 1
        ultimo_lugar_ocupado = self.__longitud - 1
        temp = self.__lista[posicion]

        while posicion != ultimo_lugar_ocupado:
            self.__lista[posicion] = self.__lista[posicion + 1]
            posicion += 1

        self.__longitud -= 1
        return temp

    def recuperar(self, posicion: int) -> object:
        if 1 > posicion > self.__longitud:
            print("posición no válida")
        return self.__lista[posicion - 1]

    def buscar(self, item: object) -> int:
        i = 0
        while i < self.__longitud and self.__lista[i] != item:
            i += 1
        return i if i != self.__longitud else -1

    def primero(self) -> object:
        return self.__lista[0]

    def ultimo(self) -> object:
        return self.__lista[self.__longitud - 1]

    def siguiente(self, posicion: int) -> int | None:
        if 1 > posicion > self.__longitud:
            print("posición no válida")
            return None
        if posicion == self.__longitud:
            print("El siguiente lugar está vacio.")
            return None
        return self.__lista[posicion]

    def anterior(self, posicion: int) -> int | None:
        if 1 > posicion > self.__longitud:
            print("posición no válida")
            return None
        posicion -= 1
        if posicion == 0:
            print("La posición ingresada es la primera, no hay anterior.")
            return None
        return self.__lista[posicion - 1]

    def mostrar(self):
        for i in range(self.__longitud):
            print(self.__lista[i], end=", ")
        print("\n")

    def vacia(self):
        return self.__longitud == 0

    def llena(self):
        return self.__longitud == self.__capacidad


if __name__ == "__main__":
    lista = ListaSecuencial(3)

    lista.insertar(1, 1)
    lista.insertar(1, 2)
    lista.insertar(1, 3)

    print(f"primero: espero: 3, obtuve: {lista.primero()}")
    print(f"ultimo: espero: 1, obtuve: {lista.ultimo()}")
    print(f"buscar: espero: 1, obtuve: {lista.buscar(2)}")
    print(f"recuperar: espero: 3, obtuve: {lista.recuperar(1)}")
    print(f"anterior: espero: 3, obtuve: {lista.anterior(2)}")
    print(f"anterior: espero: None, obtuve: {lista.anterior(1)}")
    print(f"siguiente: espero: 1, obtuve: {lista.siguiente(2)}")
    print(f"siguiente: espero: None, obtuve: {lista.siguiente(3)}")

    lista.mostrar()

    lista.eliminar(3)

    lista.mostrar()
