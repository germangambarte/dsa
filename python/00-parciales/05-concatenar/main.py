# Ejercicio 2: TAD Lista encadenada
# Codificar la operación concatenar que permita concatenar 2 listas


class Nodo:
    def __init__(self, item: int, sig=None) -> None:
        self.__item = item
        self.__sig = sig

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__sig

    def set_siguiente(self, sig: "Nodo"):
        self.__sig = sig


class Lista:
    __cabeza: Nodo | None
    __longitud: int

    def __init__(self) -> None:
        self.__cabeza = None
        self.__longitud = 0

    def insertar_contenido(self, item):
        pass

    def insertar_posicion(self, pos, item):
        pass

    def eliminar(self):
        pass

    def anterior(self):
        pass

    def siguiente(self):
        pass

    def primero(self):
        pass

    def ultimo(self):
        pass

    def buscar(self, item):
        pass

    def recuperar(self):
        pass

    def vacia(self):
        pass

    def recorrer(self):
        pass

    def concatenar_por_contenido(self, lista: "Lista"):
        actual = lista.primero()
        while actual is not None:
            self.insertar_contenido(actual)
            actual = actual.get_siguiente()

    def concatenar_por_posicion(self, lista: "Lista"):
        actual = lista.primero()
        ultimo = self.ultimo()
        i = self.buscar(ultimo)
        while actual is not None:
            self.insertar_posicion(i + 1, actual)
            actual = actual.get_siguiente()
            i += 1
