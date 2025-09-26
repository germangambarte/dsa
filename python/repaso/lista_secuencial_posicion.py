import numpy as np


class Lista:
    __cap: int
    __cab: int
    __long: int
    __lista: np.ndarray

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__long = 0
        self.__cab = 0
        self.__lista = np.empty(cap, dtype=int)

    def insertar(self, pos, item):
        if self.llena():
            print("lista llena")
            return
        pos -= 1
        if pos < 0 or pos > self.__long:
            print("posicion no válida")
            return
        i = self.__long
        while i > pos:
            self.__lista[i] = self.__lista[i - 1]
            i -= 1
        self.__lista[pos] = item
        self.__long += 1

    def eliminar(self, pos):
        if self.vacia():
            print("lista vacia.")
            return
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        temp = self.__lista[pos]
        while pos < self.__long - 1:
            self.__lista[pos] = self.__lista[pos + 1]
            pos += 1
        self.__long -= 1
        return temp

    def recorrer(self):
        i = self.__cab
        while i < self.__long:
            print(self.__lista[i], end=" ")
            i += 1
        print()

    def primero(self):
        if self.vacia():
            print("lista vacia.")
            return
        return self.__lista[0]

    def ultimo(self):
        if self.vacia():
            print("lista vacia.")
            return
        return self.__lista[self.__long - 1]

    def anterior(self, pos):
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        return None if pos - 1 == 0 else self.__lista[pos - 2]

    def siguiente(self, pos):
        if pos < 0 or pos > self.__long:
            print("posicion no válida.")
            return
        return None if pos == self.__long else self.__lista[pos]

    def recuperar(self, pos):
        if pos < 0 or pos > self.__long:
            print("posicion no válida.")
            return
        return self.__lista[pos - 1]

    def buscar(self, item):
        if self.vacia():
            print("lista vacia.")
            return
        i = 0
        while i < self.__long and self.__lista[i] != item:
            i += 1
        return None if self.__lista[i] != item else i

    def vacia(self):
        return self.__long == 0

    def llena(self):
        return self.__long == self.__cap


if __name__ == "__main__":
    lista = Lista(4)
    lista.insertar(1, 1)
    lista.insertar(1, 2)
    lista.insertar(1, 3)
    lista.insertar(1, 4)
    lista.recorrer()
    lista.eliminar(2)
    print(f"primero: {lista.primero()} == 4")
    print(f"ultimo: {lista.ultimo()} == 1")
    print(f"anterior: {lista.anterior(1)} == None")
    print(f"anterior: {lista.anterior(2)} == 4")
    print(f"siguiente: {lista.siguiente(3)} == None")
    print(f"siguiente: {lista.siguiente(2)} == 1")
    print(f"buscar: {lista.buscar(2)} == 1")
    print(f"recuperar: {lista.recuperar(3)} == 1")
    lista.recorrer()
