from arbol import Arbol


class Ejercicio(Arbol):
    def __init__(self):
        super().__init__()

    def contador_hojas(self):
        print(f"cantidad de hojas: {self._contador_hojas(self._raiz)}")

    def _contador_hojas(self, actual):
        if actual is None:
            return 0
        if self._grado(actual) == 0:
            return 1
        return self._contador_hojas(actual.get_izq()) + self._contador_hojas(actual.get_der())


if __name__ == "__main__":
    """
                  70
        47                  92

    35      68         83        100

                    79
    """
    nodos = [70, 47, 92, 35, 68, 83, 100, 79]
    arbol = Ejercicio()
    for nodo in nodos:
        arbol.insertar(nodo)
    arbol.contador_hojas()
