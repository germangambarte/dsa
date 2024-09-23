from typing import Optional


class Nodo:
    __item: int
    __siguiente: Optional["Nodo"]

    def __init__(self, item=0, siguiente=None) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def obtener_item(self):
        return self.__item

    def obtener_siguiente(self):
        return self.__siguiente

    def cargar_item(self, valor):
        self.__item = valor

    def cargar_siguiente(self, nodo):
        self.__siguiente = nodo


class PilaEncadenada:
    __tope: Optional["Nodo"]
    __cantidad: int

    def __init__(self, cant=0):
        self.__tope = None
        self.__cantidad = cant

    def insertar(self, item):
        nodo = Nodo(item, self.__tope)
        self.__tope = nodo
        self.__cantidad += 1
        return nodo.obtener_item()

    def suprimir(self):
        if self.vacia() or self.__tope == None:
            print("Pila vacia.\n")
            return None
        else:
            aux = self.__tope
            item = aux.obtener_item()
            self.__tope = self.__tope.obtener_siguiente()
            self.__cantidad -= 1
            return item

    def recorrer(self):
        actual = self.__tope
        while actual != None:
            print(actual.obtener_item(), end=" ")
            actual = actual.obtener_siguiente()
        print("\n")

    def muestra_tope(self):
        return self.__tope.obtener_item() if self.__tope else None

    def recupera_tope(self):
        return self.__tope

    def vacia(self):
        return self.__cantidad == 0


if __name__ == "__main__":
    pila = PilaEncadenada()

    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)

    pila.recorrer()

    pila.suprimir()
    pila.suprimir()

    pila.recorrer()
