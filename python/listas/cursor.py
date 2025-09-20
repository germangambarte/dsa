import numpy as np


class Celda:
    def __init__(self, item=None, siguiente=-1) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def get_item(self):
        return self.__item

    def set_item(self, item: object):
        self.__item = item

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente: int):
        self.__siguiente = siguiente


class ListaCursor:
    __cabeza: int
    __cantidad: int
    __disponible: int
    __lista: np.ndarray

    def __init__(self, capacidad: int) -> None:
        self.__lista = np.empty(capacidad, dtype=Celda)
        self.__cantidad = 0
        self.__disponible = 0
        self.__cabeza = -1
        self.inicializar()

    def inicializar(self):
        for i, _ in enumerate(self.__lista):
            self.__lista[i] = Celda(siguiente=i + 1)
        self.__lista[-1].set_siguiente(-1)

    def __buscar_disponible(self):
        if self.__disponible == -1:
            return -1
        i = self.__disponible
        self.__disponible = self.__lista[i].get_siguiente()
        return i

    def __recuperar_disponible(self, posicion: int):
        self.__lista[posicion].set_siguiente(self.__disponible)
        self.__disponible = posicion

    def insertar(self, posicion: int, item: object):
        if 1 > posicion or posicion > self.__cantidad + 1:
            print("posicion no válida.")
            return None

        nuevo = self.__buscar_disponible()
        if nuevo == -1:
            print("lista llena.")
            return None

        self.__lista[nuevo].set_item(item)

        if posicion == 1:
            self.__lista[nuevo].set_siguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            anterior = -1
            actual = self.__cabeza
            i = 1
            while i < posicion:
                anterior = actual
                actual = self.__lista[actual].get_siguiente()
                i += 1
            self.__lista[nuevo].set_siguiente(actual)
            self.__lista[anterior].set_siguiente(nuevo)

        self.__cantidad += 1

    def eliminar(self, posicion: int):
        if 1 > posicion or posicion > self.__cantidad:
            print("posicion no válida.")
            return None

        if posicion == 1:
            eliminado = self.__cabeza
            self.__cabeza = self.__lista[eliminado].get_siguiente()
        else:
            anterior = -1
            actual = self.__cabeza
            i = 1
            while i < posicion:  # avanzo hasta el nodo anterior
                anterior = actual
                actual = self.__lista[actual].get_siguiente()
                i += 1
            eliminado = actual
            self.__lista[anterior].set_siguiente(
                self.__lista[eliminado].get_siguiente()
            )

        temp = self.__lista[eliminado].get_item()
        self.__recuperar_disponible(eliminado)
        self.__cantidad -= 1
        return temp

    def recorrer(self):
        i = self.__cabeza
        while i != -1:
            print(self.__lista[i].get_item(), end=" -> ")
            i = self.__lista[i].get_siguiente()
        print("None")


if __name__ == "__main__":
    lista = ListaCursor(4)

    lista.insertar(1, 2)
    lista.insertar(1, 4)
    lista.insertar(1, 6)
    lista.recorrer()

    lista.eliminar(2)
    lista.insertar(2, 8)
    print()

    lista.recorrer()
