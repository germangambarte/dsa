import numpy as np


class Item:
    __valor: int

    def __init__(self, valor) -> None:
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor


class Tabla:
    __M: int
    __N: int
    __arreglo: np.ndarray

    def __init__(self, n) -> None:
        self.__N = n
        self.__M = self.siguiente_primo(int(self.__N / 0.7))
        self.__arreglo = np.empty(self.__M, dtype=Item)

    def es_primo(self, n):
        for i in range(2, n, 1):
            if n % i == 0:
                return False
        return True

    def siguiente_primo(self, n: int) -> int:
        while not self.es_primo(n):
            n += 1
        return n

    def hash(self, item: int):
        return item % self.__M

    def hash_alfanumerico(self, item):
        dir = 0
        for i in item:
            if i.isalpha():
                dir += ord(i)
            else:
                dir+=i
        return item % self.__M

    def hash_extraccion(self, item):
        # Suponemos que entra un documento, extraigo los ultimos 3 digitos
        extraccion = item % 1000
        print(extraccion % self.__M)
        # Suponemos que entra un documento, extraigo los primeros 3 digitos
        extraccion_2 = int(item / 1000000)
        print(extraccion_2 % self.__M)

    def hash_plegado(self,item):



    def insertar(self, item: int) -> None:
        dir = self.hash(item)

        while self.__arreglo[dir] is not None:
            dir = (dir + 1) % self.__M

        self.__arreglo[dir] = Item(item)

    def buscar(self, item: int) -> int:
        dir = self.hash(item)

        actual = self.__arreglo[dir]
        while actual and actual.get_valor() != item:
            actual = self.__arreglo[(dir + 1) % self.__M]

        return actual.get_valor() == item

    def mostrar(self) -> None:
        i = 0
        for item in self.__arreglo:
            if item is None:
                print(f"[{i}]: {item.get_valor()}")
            else:
                print(f"[{i}]: None")
            i += 1


if __name__ == "__main__":
    items = [1, 3, 5, 7, 7]
    tabla = Tabla(7)  # self.__M = 11

    for num in items:
        tabla.insertar(num)
    # tabla.mostrar()
    tabla.hash_extraccion(12345678)
    # print(tabla.buscar(5))
    # print(tabla.buscar(9))
