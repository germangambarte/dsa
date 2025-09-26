import numpy as np


class Lista:
    __lista: np.ndarray
    __cab: int
    __long: int
    __cap: int

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__long = 0
        self.__cab = 0
        self.__lista = np.empty(cap, dtype=int)

    def insertar(self, item):
        if self.llena():
            print("lista llena")
            return
        i = self.__long
        while i > self.__cab and self.__lista[i - 1] > item:
            self.__lista[i] = self.__lista[i - 1]
            i -= 1
        self.__lista[i] = item
        self.__long += 1

    def eliminar(self, item):
        if self.vacia():
            print("lista vacia.")
            return
        i = self.buscar(item)
        if i is None:
            print("item no encontrado")
            return
        temp = self.__lista[i]

        while i < self.__long - 1:
            self.__lista[i] = self.__lista[i + 1]
            i += 1
        self.__long -= 1
        return temp

    def recuperar(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return

        return self.__lista[pos]

    def buscar(self, item):
        primero = self.__cab
        ultimo = self.__long - 1
        i = None
        while primero != ultimo and i is None:
            medio = int((primero + ultimo) / 2)
            if self.__lista[medio] == item:
                i = medio
            elif self.__lista[medio] < item:
                ultimo = medio - 1
            else:
                primero = medio + 1
        return i

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
        return self.__lista[self.__cab]

    def ultimo(self):
        if self.vacia():
            print("lista vacia.")
            return
        return self.__lista[self.__long - 1]

    def anterior(self, item):
        i = self.buscar(item)
        return None if i is None or i == 0 else self.__lista[i - 1]

    def siguiente(self, item):
        i = self.buscar(item)
        return None if i is None or i == self.__long - 1 else self.__lista[i + 1]

    def llena(self):
        return self.__long == self.__cap

    def vacia(self):
        return self.__long == 0


if __name__ == "__main__":
    lista = Lista(4)
    lista.insertar(2)
    lista.insertar(1)
    lista.insertar(4)
    lista.insertar(3)
    lista.recorrer()
    lista.eliminar(2)
    print(f"primero: {lista.primero()} == 1")
    print(f"ultimo: {lista.ultimo()} == 4")
    print(f"anterior: {lista.anterior(1)} == None")
    print(f"anterior: {lista.anterior(3)} == 1")
    print(f"siguiente: {lista.siguiente(4)} == None")
    print(f"siguiente: {lista.siguiente(3)} == 4")
    print(f"buscar: {lista.buscar(3)} == 1")
    print(f"recuperar: {lista.recuperar(3)} == 4")
    lista.recorrer()
