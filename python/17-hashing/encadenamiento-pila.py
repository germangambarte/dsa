import numpy as np

class Nodo:
    def __init__(self, item, siguiente=None) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__siguiente


class Pila:
    __cantidad: int
    __cabeza: Nodo | None

    def __init__(self, cantidad=0) -> None:
        self.__cantidad = cantidad
        self.__cabeza = None

    def insertar(self, item):
        nuevo_nodo = Nodo(item, self.__cabeza)
        self.__cabeza = nuevo_nodo
        self.__cantidad += 1

    def mostrar(self):
        actual = self.__cabeza

        while actual is not None:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()

    def buscar(self, item):
        actual = self.__cabeza

        while actual is not None and actual.get_item() != item:
            actual = actual.get_siguiente()
        if actual.get_item() == item:
            return True
        else:
            return False

    def vacia(self):
        return self.__cantidad == 0

    def longitud(self):
        return self.__cantidad


class Tabla:
    __M: int
    __N: int
    __arreglo: np.ndarray

    def __init__(self, n, max_col) -> None:
        self.__N = n
        self.__M = self.siguiente_primo(int(self.__N / max_col))
        self.__arreglo = np.empty(self.__M, dtype=Pila)

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
            pila = Pila()
            pila.insertar(item)
            self.__arreglo[dir] = pila
        else:
            self.__arreglo[dir].insertar(item)

    def buscar(self, item):
        dir = self.hash(item)
        if not self.__arreglo[dir]:
            return False
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
