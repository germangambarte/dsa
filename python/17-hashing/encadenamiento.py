import numpy as np


class Nodo:
    def __init__(self, item, siguiente=None) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente

    def get_item(self):
        return self.__item

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def set_item(self, item):
        self.__item = item


class Lista:
    __cantidad: int
    __cabeza: Nodo | None
    __lista: Nodo | None

    def __init__(self) -> None:
        self.__cantidad = 0
        self.__cabeza = None
        self.__lista = None

    def insertar(self, item: object) -> None:
        nuevo_nodo = Nodo(item)
        actual = self.__cabeza
        anterior = None

        while actual is not None and actual.get_item() <= item:
            anterior = actual
            actual = actual.get_siguiente()

        if anterior is None:
            self.__cabeza = nuevo_nodo
        else:
            nuevo_nodo.set_siguiente(actual)
            anterior.set_siguiente(nuevo_nodo)
        self.__cantidad += 1

    def recuperar(self, item: object) -> object | None:
        posicion = self.buscar(item)
        i = 0
        actual = self.__cabeza
        while i != posicion:
            actual = self.__cabeza.get_siguiente()
            i += 1
        return actual.get_item() or None

    def buscar(self, item) -> int:
        actual = self.__cabeza
        i = 0

        while actual is not None and actual.get_item() != item:
            actual = actual.get_siguiente()
            i += 1

        return i if actual is not None else -1

    def mostrar(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()
        print()

    def vacia(self) -> bool:
        return self.__cantidad == 0


class Tabla:
    __M: int
    __N: int
    __arreglo: np.ndarray

    def __init__(self, n, max_col) -> None:
        self.__N = n
        self.__M = self.siguiente_primo(int(self.__N / max_col))
        self.__arreglo = np.empty(self.__M, dtype=Lista)

    def es_primo(self, n):
        for i in range(2, n, 1):
            if n % i == 0:
                return False
        return True

    def siguiente_primo(self, n):
        while not self.es_primo(n):
            n += 1
        return n

    def hash(self, item):
        return item % self.__M

    def insertar(self, item):
        dir = self.hash(item)

        if not self.__arreglo[dir]:
            lista = Lista()
            lista.insertar(item)
            self.__arreglo[dir] = lista
        else:
            self.__arreglo[dir].insertar(item)

    def buscar(self, item):
        dir = self.hash(item)
        if not self.__arreglo[dir]:
            return -1
        return self.__arreglo[dir].buscar(item)

    def mostrar(self):
        i = 0
        for lista in self.__arreglo:
            if lista is not None:
                print(f"[{i}]: ", end=" ")
                lista.mostrar()
            else:
                print(f"[{i}]: None")
            i += 1


if __name__ == "__main__":
    items = [1, 3, 5, 6, 7, 8]
    tabla = Tabla(11, 2)  # self.__M = 11

    for num in items:
        tabla.insertar(num)
    tabla.mostrar()
    print(tabla.buscar(5))
    print(tabla.buscar(9))
