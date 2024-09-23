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

    def cargar_item(self, item):
        self.__item = item

    def cargar_siguiente(self, siguiente):
        self.__siguiente = siguiente


class ColaEncadenada:
    __cantidad: int
    __primero: Nodo
    __ultimo: Nodo

    def __init__(self) -> None:
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def insertar(self, item):
        nuevo_nodo = Nodo(item)
        if self.__ultimo is None:     
            # Si la cola está vacía 
            self.__primero = nuevo_nodo
        else:
            # Si la cola no está vacía
            self.__ultimo.cargar_siguiente(nuevo_nodo)

        self.__ultimo = nuevo_nodo
        self.__cantidad += 1
        return self.__ultimo.obtener_item()

    def suprimir(self):
        if self.vacia():
            print("Cola Vacia.\n")
            return -1
        else:
            aux = Nodo(
                self.__primero.obtener_item(), self.__primero.obtener_siguiente()
            )

            self.__primero = self.__primero.obtener_siguiente()
            self.__cantidad -= 1
            if self.__primero is None:
                self.__ultimo = None
            return aux.obtener_item()

    def recuperar_primero(self):
        return self.__primero

    def recorrer(self):
        actual = self.__primero
        while actual != None:
            print(actual.obtener_item(), end=" ")
            actual = actual.obtener_siguiente()
        print("\n")

    def vacia(self):
        return self.__cantidad == 0


if __name__ == "__main__":
    pila = ColaEncadenada(4)

    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)

    pila.recorrer()

    pila.suprimir()
    pila.suprimir()

    pila.recorrer()
