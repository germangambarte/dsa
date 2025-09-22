class Termino:
    __coeficiente: int
    __exponente: int

    def __init__(self, coeficiente=0, exponente=0) -> None:
        self.__coeficiente = coeficiente
        self.__exponente = exponente

    def __repr__(self):
        return f"{self.__coeficiente}x^{self.__exponente}"

    def get_coeficiente(self):
        return self.__coeficiente

    def get_exponente(self):
        return self.__exponente

    def set_coeficiente(self, coeficiente: int):
        self.__coeficiente = coeficiente

    def set_exponente(self, exponente):
        self.__exponente = exponente


class Nodo:
    def __init__(self, item: Termino, siguiente=None) -> None:
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
    __longitud: int
    __cabeza: Nodo | None
    __lista: Nodo | None
    __max_exponente: int

    def __init__(self) -> None:
        self.__longitud = 0
        self.__cabeza = None
        self.__lista = None
        self.__max_exponente = 0

    def insertar(self, item: Termino) -> None:
        nuevo_nodo = Nodo(item)
        actual = self.__cabeza
        anterior = None

        if item.get_exponente() > self.__max_exponente:
            self.__max_exponente = item.get_exponente()

        while (
            actual is not None
            and actual.get_item().get_exponente() < item.get_exponente()
        ):
            anterior = actual
            actual = actual.get_siguiente()

        if (
            actual is not None
            and actual.get_item().get_exponente() == item.get_exponente()
        ):
            termino = actual.get_item()
            termino.set_coeficiente(termino.get_coeficiente() + item.get_coeficiente())
            return

        if anterior is None:
            nuevo_nodo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            nuevo_nodo.set_siguiente(actual)
            anterior.set_siguiente(nuevo_nodo)
        self.__longitud += 1

    def recuperar(self, item: Termino) -> Termino | None:
        posicion = self.buscar(item)
        if posicion == -1:
            return None
        i = 0
        actual = self.__cabeza
        while i < posicion:
            actual = actual.get_siguiente()
            i += 1
        return actual.get_item()

    def buscar(self, item: Termino) -> int:
        actual = self.__cabeza
        i = 0
        while (
            actual is not None
            and actual.get_item().get_exponente() != item.get_exponente()
        ):
            actual = actual.get_siguiente()
            i += 1

        return i if actual is not None else -1

    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.get_item(), end=", ")
            actual = actual.get_siguiente()
        print()

    def vacia(self) -> bool:
        return self.__longitud == 0

    def get_max_exponente(self):
        return self.__max_exponente
