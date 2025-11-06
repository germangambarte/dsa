from arbol import Arbol


class Ejercicio(Arbol):
    def __init__(self):
        super().__init__()

    def contador_descendiente_unico(self):
        print(f"nodos con unico descendiente: {self._contador_descendiente_unico(self._raiz)}")

    def _contador_descendiente_unico(self, actual):
        if actual is None:
            return 0
        if self._grado(actual) == 1:
            return 1
        return self._contador_descendiente_unico(actual.get_izq()) + self._contador_descendiente_unico(actual.get_der())


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
    arbol.contador_descendiente_unico()
