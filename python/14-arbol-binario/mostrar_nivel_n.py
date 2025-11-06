from arbol import Arbol


class Ejercicio(Arbol):
    def __init__(self):
        super().__init__()

    def mostrar_nivel(self, nivel):
        print(f"nivel {nivel}:", end=" ")
        self._mostrar_nivel(self._raiz, nivel, 1)

    def _mostrar_nivel(self, actual, nivel, nivel_actual):
        if actual is None:
            return
        self._mostrar_nivel(actual.get_izq(), nivel, nivel_actual + 1)
        if nivel == nivel_actual:
            print(actual.get_clave(), end=" ")
        self._mostrar_nivel(actual.get_der(), nivel, nivel_actual + 1)


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
    arbol.mostrar_nivel(3)
