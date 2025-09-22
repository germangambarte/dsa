class Nodo:
    def __init__(self, item, siguiente=None) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__siguiente


class Pila_Encadenada:
    __cantidad: int
    __cabeza: Nodo | None

    def __init__(self, cantidad=0) -> None:
        self.__cantidad = cantidad
        self.__cabeza = None

    def insertar(self, item):
        nuevo_nodo = Nodo(item, self.__cabeza)
        self.__cabeza = nuevo_nodo
        self.__cantidad += 1

    def eliminar(self):
        if self.__cabeza is None:
            raise IndexError("pila vacia.")
        temp = self.__cabeza.get_item()

        self.__cabeza = self.__cabeza.get_siguiente()
        self.__cantidad -= 1
        return temp

    def mostrar(self):
        actual = self.__cabeza

        while actual is not None:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()

    def vacia(self):
        return self.__cantidad == 0

    def longitud(self):
        return self.__cantidad


if __name__ == "__main__":
    pila = Pila_Encadenada(3)
    print("Agregando:")

    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)

    pila.insertar(4)
    pila.mostrar()

    print("Eliminando:")
    print(pila.eliminar())
    print(pila.eliminar())
    print(pila.eliminar())

    print(pila.eliminar())

    pila.mostrar()
