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

    def __init__(self) -> None:
        self.__cantidad = 0
        self.__cabeza = None

    def get_cabeza(self):
        return self.__cabeza

    def insertar(self, item: object) -> None:
        nuevo_nodo = Nodo(item)
        actual = self.__cabeza
        anterior = None

        while actual is not None and actual.get_item().get_nodo() <= item.get_nodo():
            anterior = actual
            actual = actual.get_siguiente()

        if anterior is None:
            self.__cabeza = nuevo_nodo
        else:
            nuevo_nodo.set_siguiente(actual)
            anterior.set_siguiente(nuevo_nodo)
        self.__cantidad += 1

    def eliminar(self, item: int) -> object | None:
        actual = self.__cabeza
        anterior = None
        while actual is not None and actual.get_item() != item:
            anterior = actual
            actual = actual.get_siguiente()

        if actual is None:
            print("elemento no encontrado.")
            return None

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

    def anterior(self, item:object) -> object | None:
        anterior = None
        actual = self.__cabeza
        while actual and actual.get_item() != item:
            anterior = actual
            actual = self.__cabeza.get_siguiente()
        return anterior.get_item() if anterior is not None else None

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
        return (
            actual.get_siguiente().get_item()
            if actual.get_siguiente() is not None
            else None
        )

    def recuperar(self, item:object) -> object | None:
        posicion = self.buscar(item)
        i = 0
        actual = self.__cabeza
        while posicion is not None and i != posicion:
            actual = actual.get_siguiente()
            i += 1
        return actual.get_item() if actual is not None else None

    def buscar(self, item:object) -> int | None:
        actual = self.__cabeza
        i = 0

        while actual is not None and actual.get_item().get_nodo() != item:
            actual = actual.get_siguiente()
            i += 1

        return i if actual is not None else None

    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            item =  actual.get_item()
            print(f"({item.get_nodo()}, {item.get_peso()})", end=" ")
            actual = actual.get_siguiente()
        print()

    def vacia(self) -> bool:
        return self.__cantidad == 0


if __name__ == "__main__":
    lista = Lista()
    lista.insertar(1)
    lista.insertar(3)
    lista.insertar(2)

    lista.recorrer()

    print(f"primero: espero: 1, obtuve: {lista.primero()}")
    print(f"ultimo: espero: 3, obtuve: {lista.ultimo()}")
    print(f"buscar: espero: 1, obtuve: {lista.buscar(2)}")
    print(f"recuperar: espero: 1, obtuve: {lista.recuperar(1)}")
    print(f"anterior: espero: 1, obtuve: {lista.anterior(2)}")
    print(f"anterior: espero: None, obtuve: {lista.anterior(1)}")
    print(f"siguiente: espero: 3, obtuve: {lista.siguiente(2)}")
    print(f"siguiente: espero: None, obtuve: {lista.siguiente(3)}")

    lista.eliminar(3)

    lista.recorrer()
