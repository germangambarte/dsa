from pilas.secuencial import Pila_Secuencial


def recursion(n: int, solution=""):
    if n == 0:
        print(solution)
        return
    if n == 1:
        print(solution + "1")
        return
    recursion(n - 1, solution + "1")
    recursion(n - 2, solution + "2")


def buscar_soluciones(ps: Pila_Secuencial):
    while not ps.vacia():
        n, solucion = ps.eliminar() or (0, "")
        if n == 0:
            print(solucion)
        elif n == 1:
            ps.insertar((n - 1, solucion + "1"))
        else:
            ps.insertar((n - 1, solucion + "1"))
            ps.insertar((n - 2, solucion + "2"))


if __name__ == "__main__":
    ps = Pila_Secuencial(10)
    print("Solución recursiva: ")
    recursion(4, "")
    print("Solución no recursiva: ")
    ps.insertar((4, ""))
    buscar_soluciones(ps)
