from nodo import Nodo


class Arbol:
    _raiz: Nodo

    def __init__(self):
        self._raiz = None

    def insertar(self, clave):
        self._raiz = self._insertar(self._raiz, clave)

    def _insertar(self, actual, clave):
        if actual is None:
            actual = Nodo(clave)
        elif actual.get_clave() > clave:
            actual.set_izq(self._insertar(actual.get_izq(), clave))
        else:
            actual.set_der(self._insertar(actual.get_der(), clave))
        return actual

    def suprimir(self, clave):
        self._raiz = self._suprimir(self._raiz, clave)

    def _suprimir(self, actual, clave: int):
        if actual is None:
            return None
        elif actual.get_clave() > clave:
            actual.set_izq(self._suprimir(actual.get_izq(), clave))
        elif actual.get_clave() < clave:
            actual.set_der(self._suprimir(actual.get_der(), clave))
        else:
            grado = self._grado(actual)
            if grado == 0:
                return None
            elif grado == 2:
                actual.set_clave(self.__maximo(actual.get_izq()))
                actual.set_izq(self._suprimir(actual.get_izq(), actual.get_clave()))
            else:
                if actual.get_izq() is not None:
                    return actual.get_izq()
                else:
                    return actual.get_der()

        return actual

    def _grado(self, nodo):
        grado = 0
        if nodo.get_izq() is not None:
            grado += 1
        if nodo.get_der() is not None:
            grado += 1
        return grado

    def __maximo(self, actual):
        if actual.get_der() is None:
            return actual.get_clave()
        return self.__maximo(actual.get_der())

    def inorden(self):
        self._inorden(self._raiz)

    def _inorden(self, actual):
        if actual is None:
            return
        self._inorden(actual.get_izq())
        print(actual.get_clave())
        self._inorden(actual.get_der())

    def buscar(self, clave):
        resultado = self._buscar(self._raiz, clave)
        if resultado is not None:
            print("Encontrado.")
        else:
            print("No encontrado.")
        return resultado if resultado else None

    def _buscar(self, actual, clave):
        if clave is None:
            return None
        if actual.get_clave() == clave:
            return actual
        elif actual.get_clave() > clave:
            return self._buscar(actual.get_izq(), clave)
        else:
            return self._buscar(actual.get_der(), clave)

    def hijo(self, hijo, padre):
        print(f"{hijo} hijo de {padre}: {self._hijo(self._raiz, hijo, padre)}")

    def _hijo(self, actual, hijo, padre):
        if actual is None:
            return False
        if actual.get_clave() == padre:
            return actual.get_izq().get_clave() == hijo or actual.get_der().get_clave() == hijo
        if actual.get_clave() > padre:
            return self._hijo(actual.get_izq(), hijo, padre)
        else:
            return self._hijo(actual.get_der(), hijo, padre)

    def padre(self, padre, hijo):
        print(f"{padre} padre de {hijo}: {self._padre(self._raiz, padre, hijo)}")

    def _padre(self, actual, padre, hijo):
        if actual is None:
            return False
        if actual.get_clave() == padre:
            return actual.get_izq().get_clave() == hijo or actual.get_der().get_clave() == hijo
        if actual.get_clave() > padre:
            return self._padre(actual.get_izq(), padre, hijo)
        else:
            return self._padre(actual.get_der(), padre, hijo)

    def nivel(self, clave):
        print(f"nivel {self._nivel(self._raiz, clave, 0)}")

    def _nivel(self, actual, clave, nivel):
        if actual.get_clave() == clave:
            return nivel
        if actual.get_clave() > clave:
            return self._nivel(actual.get_izq(), clave, nivel + 1)
        else:
            return self._nivel(actual.get_der(), clave, nivel + 1)

    def hoja(self, clave):
        print(f"{clave} es hoja: {self._hoja(self._raiz, clave)}")

    def _hoja(self, actual, clave):
        if actual.get_clave() == clave:
            return self._grado(actual) == 0
        if actual.get_clave() > clave:
            return self._hoja(actual.get_izq(), clave)
        else:
            return self._hoja(actual.get_der(), clave)

    def altura(self):
        print(f"altura: {self._altura(self._raiz)}")

    def _altura(self, actual):
        if actual is None:
            return -1
        altura_izq = self._altura(actual.get_izq())
        altura_der = self._altura(actual.get_der())
        return 1 + max(altura_der, altura_izq)

    def camino(self, origen: int, destino: int):
        origen_nodo = self._buscar(self._raiz, origen)

        if origen_nodo is None:
            print("origen no encontrado.")
            return

        print(f"camino:", end=" ")
        print(self._camino(origen_nodo, destino))

    def _camino(self, actual, destino):
        if actual is None:
            return
        if actual.get_clave() == destino:
            print(actual.get_clave())
            return
        print(actual.get_clave(), end=" ")
        if actual.get_clave() > destino:
            self._camino(actual.get_izq(), destino)
        else:
            self._camino(actual.get_der(), destino)


if __name__ == "__main__":
    """
                  70
        47                  92

    35      68         83        100

                    79
    """

    nodos = [70, 47, 92, 35, 68, 83, 100, 79]
    arbol = Arbol()
    for nodo in nodos:
        arbol.insertar(nodo)
    arbol.hijo(83, 92)
    arbol.padre(92, 83)
    arbol.nivel(83)
    arbol.hoja(79)
    arbol.altura()
    arbol.camino(92, 79)
    arbol.inorden()
