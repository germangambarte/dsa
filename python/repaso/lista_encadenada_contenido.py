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
        self.__cab = None
        self.__long = 0

    def insertar(self, item):
        nuevo = Nodo(item)
        anterior = None
        actual = self.__cab
        while actual and actual.get_item() < item:
            anterior = actual
            actual = actual.get_sig()
        if anterior is None:
            nuevo.set_sig(self.__cab)
            self.__cab = nuevo
        else:
            anterior.set_sig(nuevo)
            nuevo.set_sig(actual)
        self.__long += 1

    def eliminar(self, item):
        if self.vacia():
            print("lista vacia.")
            return
        anterior = None
        actual = self.__cab
        while actual and actual.get_item() < item:
            anterior = actual
            actual = actual.get_sig()
        temp = actual
        if anterior is None:
            self.__cab = self.__cab.get_sig()
        else:
            anterior.set_sig(actual.get_sig())
        self.__long -= 1
        return actual.get_item()

    def anterior(self, item):
        if self.vacia():
            print("lista vacia.")
            return
        anterior = None
        actual = self.__cab
        while actual and actual.get_item() != item:
            anterior = actual
            actual = actual.get_sig()

        return None if anterior is None else anterior.get_item()

    def siguiente(self, item):
        actual = self.__cab
        siguiente = None
        while actual and actual.get_item() != item:
            actual = actual.get_sig()
            siguiente = actual.get_sig()
        return None if siguiente is None else siguiente.get_item()

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

    def buscar(self, item):
        if self.vacia():
            return
        actual = self.__cab
        i = 0
        while actual and actual.get_item() != item:
            actual = actual.get_sig()
            i += 1
        return None if actual is None else i

    def recuperar(self, pos):
        pos -= 1
        if pos < 0 and pos >= self.__long:
            print("pocision no válida")
            return
        actual = self.__cab
        i = 0
        while actual and i < pos:
            actual = actual.get_sig()
            i += 1
        return None if actual is None else actual.get_item()

    def recorrer(self):
        actual = self.__cab
        while actual:
            print(actual.get_item(), end=" ")
            actual = actual.get_sig()
        print()

    def vacia(self):
        return self.__long == 0

    def eliminar_repetidos(self):
        aux = Lista()  # creo una nueva lista, vacía
        actual = self.__cab  # tomo la cabeza de mi lista cargada, la original
        while actual:
            existe = aux.buscar(actual.get_item())  # busco el elemento en mi lista aux
            if existe is None:  # Si el elemento no está en mi lista aux lo meto
                aux.insertar(actual.get_item())
            else:  # Si elemento está en mi lista aux, lo elimino de mi lista original
                self.eliminar(actual.get_item())
            actual = actual.get_sig()  # paso al siguiente elemento


if __name__ == "__main__":
    lista = Lista()
    lista.insertar(2)
    lista.insertar(1)
    lista.insertar(1)
    lista.insertar(4)
    lista.insertar(3)
    lista.insertar(3)
    print("lista con repetidos: ", end=" ")
    lista.recorrer()
    lista.eliminar_repetidos()
    print("lista sin repetidos: ", end=" ")
    lista.recorrer()
