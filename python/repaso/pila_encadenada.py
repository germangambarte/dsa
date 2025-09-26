class Nodo:
    __item: int
    __sig: "Nodo | None"

    def __init__(self, item: int, sig=None) -> None:
        self.__item = item
        self.__sig = sig

    def get_item(self):
        return self.__item

    def set_sig(self, sig):
        self.__sig = sig

    def get_sig(self):
        return self.__sig


class Pila:
    __cab: Nodo | None
    __long: int

    def __init__(self) -> None:
        self.__cab = None
        self.__long = 0

    def insertar(self, item):
        nuevo = Nodo(item, self.__cab)
        self.__cab = nuevo
        self.__long += 1

    def eliminar(self):
        if self.vacia():
            print("pila vacia.")
            return
        temp = self.__cab
        self.__cab = self.__cab.get_sig()
        self.__long -= 1
        return temp.get_item()

    def recorrer(self):
        actual = self.__cab
        while actual:
            print(actual.get_item(), end=" ")
            actual = actual.get_sig()
        print()

    def vacia(self):
        return self.__long == 0


if __name__ == "__main__":
    pila = Pila()
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)

    pila.recorrer()

    pila.eliminar()

    pila.recorrer()
