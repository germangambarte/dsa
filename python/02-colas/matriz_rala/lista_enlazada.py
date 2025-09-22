class Celda:
    def __init__(self, componente, fila, columna) -> None:
        self.__componente = componente
        self.__fila = fila
        self.__columna = columna

    def get_componente(self):
        return self.__componente

    def get_columna(self):
        return self.__columna

    def get_fila(self):
        return self.__fila

    def set_componente(self, componente):
        self.__componente = componente


class Nodo:
    def __init__(self, item: Celda, siguiente=None) -> None:
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
    __ultimo: Nodo | None

    def __init__(self) -> None:
        self.__longitud = 0
        self.__cabeza = None
        self.__ultimo = None

    def insertar(self, posicion: int, item: Celda) -> None:
        if posicion < 1 or posicion > self.__longitud + 1:
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
        self.__longitud += 1

    def eliminar(self, posicion: int):
        if posicion < 1 or posicion > self.__longitud + 1:
            print("posición no válida.")
            return None
        actual = self.__cabeza
        anterior = None
        i = 0
        while i < posicion - 1 and actual is not None:
            anterior = actual
            actual = actual.get_siguiente()
            i += 1
        temp = actual.get_item()
        if anterior is None:
            self.__cabeza = actual.get_siguiente()
        else:
            anterior.set_siguiente(actual.get_siguiente())
        self.__longitud -= 1
        return temp

    def recuperar(self, posicion) -> Celda | None:
        if posicion < 1 or posicion > self.__longitud:
            print("posición no válida.")
            return None
        i = 1
        actual = self.__cabeza
        while i < posicion:
            actual = actual.get_siguiente()
            i += 1
        return actual.get_item() or None

    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.get_item().get_componente(), end=" ")
            actual = actual.get_siguiente()
        print()

    def vacia(self) -> bool:
        return self.__longitud == 0

    def get_longitud(self):
        return self.__longitud
