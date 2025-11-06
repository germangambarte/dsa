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
            nuevo_nodo.set_siguiente(self.__cabeza)  # 👈 Enlaza el resto de la lista
            self.__cabeza = nuevo_nodo
        else:
            nuevo_nodo.set_siguiente(actual)
            anterior.set_siguiente(nuevo_nodo)
        self.__cantidad += 1

    # def insertar(self, item: object) -> None:
    #     nuevo_nodo = Nodo(item)
    #     actual = self.__cabeza
    #     anterior = None
    #
    #     while actual is not None and actual.get_item() <= item:
    #         anterior = actual
    #         actual = actual.get_siguiente()
    #
    #     if anterior is None:
    #         self.__cabeza = nuevo_nodo
    #     else:
    #         nuevo_nodo.set_siguiente(actual)
    #         anterior.set_siguiente(nuevo_nodo)
    #     self.__cantidad += 1

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
