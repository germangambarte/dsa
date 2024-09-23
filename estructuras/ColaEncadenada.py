class Nodo:
    __item: int
    __siguiente: "Nodo"

    def __init__(self, item=0, siguiente=None):
        self.__item = item
        self.__siguiente = siguiente

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__siguiente

    def set_item(self, item):
        self.__item = item

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente


class ColaEncadenada:
    __dimension: int
    __cantidad: int
    __ultimo: Nodo
    __primero: Nodo

    def __init__(self, dim):
        self.__dimension = dim
        self.__cantidad = 0
        self.__ultimo = None
        self.__primero = None

    def insertar(self, item):
        if self.__cantidad == self.__dimension:
            print("Cola llena.")
            return None
        nuevo_nodo = Nodo(item)
        if self.__ultimo is None:
            self.__primero = nuevo_nodo
        else:
            self.__ultimo.set_siguiente(nuevo_nodo)
        self.__ultimo = nuevo_nodo
        self.__cantidad += 1
        return self.__ultimo.get_item()

    def suprimir(self):
        if self.vacia():
            print("Cola vacia.")
            return None
        eliminado = self.__primero
        self.__primero = self.__primero.get_siguiente()
        self.__cantidad -= 1
        return eliminado.get_item()

    def recorrer(self):
        if self.vacia():
            print("Cola vacia.")
            return None
        actual = self.__primero
        while actual is not None:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()
        print("\n")

    def vacia(self):
        return self.__cantidad == 0


if __name__ == "__main__":
    cola = ColaEncadenada(4)

    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)

    cola.recorrer()

    cola.suprimir()
    cola.suprimir()

    cola.recorrer()
