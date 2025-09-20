class Nodo:
    def __init__(self, item: object, siguiente=None) -> None:
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


class ListaEnlazadaPosicion:
    __cantidad: int
    __cabeza: Nodo | None
    __lista: Nodo | None
    __ultimo: Nodo | None

    def __init__(self) -> None:
        self.__cantidad = 0
        self.__cabeza = None
        self.__lista = None

    def insertar(self, posicion: int, item: object) -> None:
        if 1 > posicion < self.__cantidad:
            print("posición no válida.")
            return None
        posicion -= 1
        actual = self.__cabeza
        anterior = None
        i = 0
        while i != posicion and actual is not None:
            anterior = actual
            actual = actual.get_siguiente()
            i += 1
        nuevo_nodo = Nodo(item, actual)
        if anterior is None:
            self.__cabeza = nuevo_nodo
        else:
            anterior.set_siguiente(nuevo_nodo)
        self.__cantidad += 1

    def eliminar(self, posicion: int):
        if 1 > posicion < self.__cantidad:
            print("posición no válida.")
            return None
        posicion -= 1
        actual = self.__cabeza
        anterior = None
        i = 0
        while i != posicion and actual is not None:
            anterior = actual
            actual = actual.get_siguiente()
            i += 1
        temp = actual.get_item()
        if anterior is None:
            self.__cabeza = actual.get_siguiente()
        else:
            anterior.set_siguiente(actual.get_siguiente())
        self.__cantidad -= 1
        return temp

    def primero(self) -> object | None:
        return self.__cabeza.get_item() or None

    def ultimo(self) -> object | None:
        actual = self.__cabeza
        while actual and actual.get_siguiente() is not None:
            actual = actual.get_siguiente()
        return actual.get_item() or None

    def anterior(self, posicion) -> object | None:
        if 1 > posicion < self.__cantidad:
            print("posición no válida.")
            return None
        posicion -= 1
        i = 0
        anterior = None
        actual = self.__cabeza
        while i != posicion:
            anterior = actual
            actual = self.__cabeza.get_siguiente()
            i += 1
        return anterior.get_item()if anterior is not None else None

    def siguiente(self, posicion) -> object | None:
        if 1 > posicion < self.__cantidad:
            print("posición no válida.")
            return None
        posicion -= 1
        i = 0
        actual = self.__cabeza
        while i != posicion:
            actual = actual.get_siguiente()
            i += 1
        return actual.get_siguiente().get_item() if actual.get_siguiente() is not None else None

    def recuperar(self, posicion) -> object | None:
        if 1 > posicion < self.__cantidad:
            print("posición no válida.")
            return None
        posicion -= 1
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

    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()
        print()

    def vacia(self) -> bool:
        return self.__cantidad == 0


if __name__ == "__main__":
    lista = ListaEnlazadaPosicion()
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

    lista.recorrer()

    lista.eliminar(3)

    lista.recorrer()
