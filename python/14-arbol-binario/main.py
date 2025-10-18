class Nodo:
    clave: int
    izq: "Nodo | None"
    der: "Nodo | None"

    def __init__(self, clave, izq=None, der=None) -> None:
        self.clave = clave
        self.der = der
        self.izq = izq

    def get_izq(self):
        return self.izq

    def get_der(self):
        return self.der

    def get_clave(self):
        return self.clave

    def set_izq(self, izq):
        self.izq = izq

    def set_der(self, der):
        self.der = der

    def set_clave(self, clave):
        self.clave = clave

    def __lt__(self, otro):
        if isinstance(otro, Nodo):
            return self.clave < otro.clave
        return self.clave < otro

    def __gt__(self, otro):
        if isinstance(otro, Nodo):
            return self.clave > otro.clave
        return self.clave > otro

    def __eq__(self, otro):
        if isinstance(otro, Nodo):
            return self.clave == otro.clave
        return self.clave == otro

    def __repr__(self):
        return f"{self.clave}"


class ArbolBinarioBusqueda:
    __raiz: Nodo | None

    def __init__(self) -> None:
        self.__raiz = None

    def __es_igual(self, nodo: Nodo | None, clave: int):
        return nodo and nodo.get_clave() == clave

    def in_orden(self):
        self.__in_orden(self.__raiz)
        print()

    def __in_orden(self, actual=None):
        if actual is None:
            return
        self.__in_orden(actual.get_izq())
        print(actual, end=" ")
        self.__in_orden(actual.get_der())

    def buscar(self, item):
        return self.__buscar(self.__raiz, item)

    def __buscar(self, actual, item):
        if actual is None:
            return False
        if actual == item:
            return True
        if actual > item:
            return self.__buscar(actual.get_izq(), item)
        else:
            return self.__buscar(actual.get_der(), item)

    def buscar_alt(self, item: int) -> Nodo | None:
        return self.__buscar_alt(self.__raiz, item)

    def __buscar_alt(self, actual, item):
        if actual is None:
            return None
        if actual == item:
            return actual
        if actual > item:
            return self.__buscar_alt(actual.get_izq(), item)
        else:
            return self.__buscar_alt(actual.get_der(), item)

    def __minimo(self, actual):
        if not actual.get_izq():
            return actual
        self.__minimo(actual.get_izq())

    def __maximo(self, actual):
        if not actual.get_der():
            return actual
        return self.__maximo(actual.get_der())

    def insertar(self, item):
        self.__raiz = self.__insertar(self.__raiz, item)

    def __insertar(self, actual, item):
        if not actual:
            return Nodo(item)
        if actual > item:
            actual.set_izq(self.__insertar(actual.get_izq(), item))
        else:
            actual.set_der(self.__insertar(actual.get_der(), item))
        return actual

    def __grado(self, nodo):
        grado = 0
        if nodo.get_izq():
            grado += 1
        if nodo.get_der():
            grado += 1
        return grado

    def suprimir(self, item):
        self.__raiz = self.__suprimir(self.__raiz, item)

    def __suprimir(self, actual, item):
        if not actual:
            return None
        if actual > item:
            actual.get_izq(self.__suprimir(actual.get_izq(), item))
        elif actual < item:
            actual.get_der(self.__suprimir(actual.get_der(), item))
        else:
            grado = self.__grado(actual)
            if grado == 0:
                return None
            elif grado == 1:
                if actual.get_izq():
                    return actual.get_izq()
                else:
                    return actual.get_der()
            else:
                max = self.__maximo(actual.get_izq())
                actual.set_clave(max.get_clave())
                actual.set_izq(self.__suprimir(actual.get_izq(), actual.get_clave()))
        return actual

    def camino(self, inicio: int, fin: int):
        nodo_inicio = self.buscar_alt(inicio)
        if nodo_inicio is None:
            print(f"nodo {inicio} no existe.")
        else:
            self.__camino(nodo_inicio, fin)

    def __camino(self, actual: Nodo, fin: int):
        if actual == fin:
            print(actual)
            return
        print(f"{actual}", end=" -> ")
        if actual > fin:
            self.__camino(actual.get_izq(), fin)
        else:
            self.__camino(actual.get_der(), fin)

    def hijo(self, padre: int, hijo: int):
        return self.__hijo(self.__raiz, padre, hijo)

    def __hijo(self, actual: Nodo | None, padre: int, hijo: int):
        if actual is None:
            return False
        if actual == padre:
            return self.__es_igual(actual.get_izq(), hijo) or self.__es_igual(
                actual.get_der(), hijo
            )
        if actual > padre:
            return self.__hijo(actual.get_izq(), padre, hijo)
        else:
            return self.__hijo(actual.get_der(), padre, hijo)

    def padre(self, padre: int, hijo: int):
        return self.__padre(self.__raiz, padre, hijo)

    def __padre(self, actual: Nodo, padre: int, hijo: int):
        if self.__grado(actual) == 0:
            return False
        if actual == padre:
            return self.__es_igual(actual.get_izq(), hijo) or self.__es_igual(
                actual.get_der(), hijo
            )
        if actual > padre:
            return self.__hijo(actual.get_izq(), padre, hijo)
        else:
            return self.__hijo(actual.get_der(), padre, hijo)

    def __nivel(self, actual: Nodo, clave: int, contador=0):
        if actual == clave:
            print(f"nivel de {clave}: {contador}")
            return
        if actual > clave:
            self.__nivel(actual.get_izq(), clave, contador + 1)
        else:
            self.__nivel(actual.get_der(), clave, contador + 1)

    def hoja(self, clave: int):
        nodo = self.buscar_alt(clave)
        if not nodo:
            print(f"nodo {clave} no encontrado")
            return
        return self.__grado(nodo) == 2

    def altura(self):
        return self.__altura(self.__raiz)

    def __altura(self, actual: Nodo | None):
        if not actual:
            return -1
        alt_izq = self.__altura(actual.get_izq())
        alt_der = self.__altura(actual.get_der())
        return 1 + max(alt_izq, alt_der)


if __name__ == "__main__":
    """
                  70
        47                  92

    35      68         83        100

                    79
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(70)
    arbol.insertar(47)
    arbol.insertar(92)
    arbol.insertar(35)
    arbol.insertar(68)
    arbol.insertar(83)
    arbol.insertar(100)
    arbol.insertar(79)
    arbol.in_orden()
