from pilas.encadenada import Pila_Encadenada

def recursion(n: int, solution=""):
    if n == 0:
        print(solution)
        return
    if n == 1:
        print(solution + "1")
        return
    recursion(n - 1, solution + "1")
    recursion(n - 2, solution + "2")


def buscar_soluciones(pe: Pila_Encadenada):
    while not pe.vacia():
        n, solucion = pe.eliminar()
        if n == 0:
            print(solucion)
        elif n == 1:
            pe.insertar((n - 1, solucion + "1"))
        else:
            pe.insertar((n - 1, solucion + "1"))
            pe.insertar((n - 2, solucion + "2"))


if __name__ == "__main__":
    pe = Pila_Encadenada()
    print("Solución recursiva: ")
    recursion(4, "")
    print("Solución no recursiva: ")
    pe.insertar((4, ""))
    buscar_soluciones(pe)
