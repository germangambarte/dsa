class Nodo:
    __item: int
    __sig: "Nodo | None"

    def __init__(self, item, sig=None) -> None:
        self.__item = item
        self.__sig = sig

    def get_item(self):
        return self.__item

    def set_sig(self, sig):
        self.__sig = sig

    def get_sig(self):
        return self.__sig


class Cola:
    __pri: Nodo | None
    __ult: Nodo | None
    __long: int

    def __init__(self) -> None:
        self.__pri = None
        self.__ult = None
        self.__long = 0

    def insertar(self, item):
        nuevo = Nodo(item)
        if self.vacia():
            self.__pri = nuevo
        else:
            self.__ult.set_sig(nuevo)
        self.__ult = nuevo
        self.__long += 1

    def eliminar(self):
        if self.vacia():
            print("cola vacia")
            return
        temp = self.__pri
        self.__pri = self.__pri.get_sig()
        self.__long -= 1
        return temp.get_item()

    def recorrer(self):
        actual = self.__pri
        while actual:
            print(actual.get_item(), end=" ")
            actual = actual.get_sig()
        print()

    def vacia(self):
        return self.__long == 0


if __name__ == "__main__":
    cola = Cola()
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)

    cola.recorrer()

    cola.eliminar()

    cola.recorrer()
