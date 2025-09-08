import numpy as np


class ListaSecuencial:
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

    def eliminar(self, item: int) -> object | None:
        if self.vacia():
            print("lista vacia.")
            return None
        posicion = self.buscar(item)
        if posicion is None:
            print("El item no está en la lista.")
            return
        temp = self.__lista[posicion]
        while posicion != self.__longitud - 1:
            self.__lista[posicion] = self.__lista[posicion + 1]
            posicion += 1

        self.__longitud -= 1
        return temp

    def recuperar(self, posicion: int) -> object:
        if 1 > posicion > self.__longitud:
            print("posición no válida")
        return self.__lista[posicion - 1]

    def buscar(self, item: object) -> int | None:
        primero = 0
        ultimo = self.__longitud - 1
        i = None
        while primero != ultimo and i is None:
            medio = int((primero + ultimo) / 2)
            if item == self.__lista[medio]:
                i = medio
            elif item < self.__lista[medio]:
                ultimo = medio - 1
            else:
                primero = medio + 1
        return i

    def primero(self) -> object:
        return self.__lista[0]

    def ultimo(self) -> object:
        return self.__lista[self.__longitud - 1]

    def siguiente(self, item: int) -> int | None:
        posicion = self.buscar(item)

        if posicion is None:
            print("Item no encontrado.")
            return None

        if posicion == self.__longitud:
            print("No hay item siguiente.")
            return None

        return self.__lista[posicion + 1]

    def anterior(self, item: int) -> int | None:
        posicion = self.buscar(item)

        if posicion is None:
            print("Item no encontrado.")
            return None

        if posicion == self.__longitud:
            print("No hay item siguiente.")
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
    lista = ListaSecuencial(4)

    lista.insertar(1)
    lista.insertar(3)
    lista.insertar(4)
    lista.insertar(2)

    print(f"primero: espero: 1, obtuve: {lista.primero()}")
    print(f"ultimo: espero: 4, obtuve: {lista.ultimo()}")
    print(f"buscar: espero: 1, obtuve: {lista.buscar(2)}")
    print(f"recuperar: espero: 1, obtuve: {lista.recuperar(1)}")
    print(f"anterior: espero: 1, obtuve: {lista.anterior(2)}")
    print(f"anterior: espero: None, obtuve: {lista.anterior(1)}")
    print(f"siguiente: espero: 3, obtuve: {lista.siguiente(2)}")
    print(f"siguiente: espero: None, obtuve: {lista.siguiente(3)}")

    lista.mostrar()
    lista.eliminar(3)
    lista.mostrar()
