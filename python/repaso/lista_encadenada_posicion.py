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


class Lista:
    __cab: Nodo | None
    __long: int

    def __init__(self) -> None:
        self.__long = 0
        self.__cab = None

    def insertar(self, pos, item):
        pos -= 1
        if pos < 0 or pos > self.__long:
            print("posicion no válida.")
            return

        nuevo = Nodo(item)
        i = 0
        anterior = None
        actual = self.__cab
        while i < pos:
            anterior = actual
            actual = actual.get_sig()
            i += 1
        if anterior is None:
            nuevo.set_sig(self.__cab)
            self.__cab = nuevo
        else:
            nuevo.set_sig(actual)
            anterior.set_sig(nuevo)
        self.__long += 1

    def eliminar(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        i = 0
        anterior = None
        actual = self.__cab
        while actual and i < pos:
            anterior = actual
            actual = actual.get_sig()
            i += 1
        temp = actual
        if anterior is None:
            self.__cab = self.__cab.get_sig()
        else:
            anterior.set_sig(actual.get_sig())
        self.__long -= 1

    def buscar(self, item):
        i = 0
        actual = self.__cab
        while actual and actual.get_item() != item:
            actual = actual.get_sig()
            i += 1
        return None if i >= self.__long else i

    def recuperar(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        i = 0
        actual = self.__cab
        while actual and i < pos:
            actual = actual.get_sig()
            i += 1
        return i

    def primero(self):
        if self.vacia():
            print("lista vacia.")
            return
        return self.__cab.get_item()

    def ultimo(self):
        if self.vacia():
            print("lista vacia.")
            return
        anterior = None
        actual = self.__cab
        while actual:
            anterior = actual
            actual = actual.get_sig()
        return anterior.get_item()

    def anterior(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        i = 0
        anterior = None
        actual = self.__cab
        while actual and i < pos:
            anterior = actual
            actual = actual.get_sig()
            i += 1
        return None if anterior is None else anterior.get_item()

    def siguiente(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__long:
            print("posicion no válida.")
            return
        i = 0
        actual = self.__cab
        siguiente = None
        while actual and i < pos:
            actual = actual.get_sig()
            siguiente = actual.get_sig()
            i += 1
        return None if siguiente is None else siguiente.get_item()

    def recorrer(self):
        actual = self.__cab
        while actual:
            print(actual.get_item(), end=" ")
            actual = actual.get_sig()
        print()

    def vacia(self):
        return self.__long == 0


if __name__ == "__main__":
    lista = Lista()
    lista.insertar(1, 1)
    lista.insertar(1, 2)
    lista.insertar(1, 3)
    lista.insertar(1, 4)
    lista.recorrer()
    lista.eliminar(2)
    print(f"primero: {lista.primero()} == 4")
    print(f"ultimo: {lista.ultimo()} == 1")
    print(f"anterior: {lista.anterior(1)} == None")
    print(f"anterior: {lista.anterior(2)} == 4")
    print(f"siguiente: {lista.siguiente(3)} == None")
    print(f"siguiente: {lista.siguiente(2)} == 1")
    print(f"buscar: {lista.buscar(4)} == 0")
    print(f"recuperar: {lista.recuperar(2)} == 1")
    lista.recorrer()
