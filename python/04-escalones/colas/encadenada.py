class Nodo: def __init__(self, item, siguiente=None):
        self.item = item
        self.siguiente = siguiente

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente


class Cola_Encadenada:
    __cabeza: Nodo | None
    __cola: Nodo | None
    __cantidad: int

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cola = None
        self.__cantidad = 0

    def insertar(self, item):
        nuevo_nodo = Nodo(item)
        if self.__cola is None:
            self.__cabeza = nuevo_nodo
        else:
            self.__cola.set_siguiente(nuevo_nodo)
        self.__cola = nuevo_nodo
        self.__cantidad += 1

    def eliminar(self):
        if self.vacia():
            print("cola vacia.")
            return
        temp = self.__cabeza
        self.__cabeza = self.__cabeza.get_siguiente()
        self.__cantidad -= 1
        if self.__cabeza is None:
            self.__cola = None
        return temp.get_item()

    def mostrar(self):
        actual = self.__cabeza

        while actual is not None:
            print(actual.get_item())
            actual = actual.get_siguiente()

    def vacia(self):
        return self.__cantidad == 0

    def obtener_cantidad(self):
        return self.__cantidad


if __name__ == "__main__":
    cola = Cola_Encadenada()

    print("Insertar:")
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)

    cola.mostrar()

    print("Eliminar:")
    cola.eliminar()
    cola.eliminar()

    cola.mostrar()
