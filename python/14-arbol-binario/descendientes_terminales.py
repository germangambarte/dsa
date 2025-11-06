from arbol import Arbol


class Ejercicio(Arbol):
    def __init__(self):
        super().__init__()

    def descendientes_terminales(self, clave):
        print(f"nodos terminales de {clave}:", end=" ")
        nodo = self._buscar(self._raiz, clave)
        self._descendientes_terminales(nodo)

    def _descendientes_terminales(self, actual):
        if actual is None:
            return
        self._descendientes_terminales(actual.get_izq())
        if self._grado(actual) == 0:
            print(actual.get_clave(), end=" ")
        self._descendientes_terminales(actual.get_der())


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
    arbol.descendientes_terminales(70)
