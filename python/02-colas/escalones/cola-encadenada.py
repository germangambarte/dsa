from colas.encadenada import Cola_Encadenada


class Camino:
    n: int
    solucion: str

    def __init__(self, n, solucion="") -> None:
        self.n = n
        self.solucion = solucion


def obtener_caminos(cola: Cola_Encadenada):
    while not cola.vacia():
        camino = cola.eliminar()
        if camino.n == 0:
            print(camino.solucion)
        elif camino.n == 1:
            cola.insertar(Camino(camino.n - 1, camino.solucion + "1"))
        else:
            cola.insertar(Camino(camino.n - 1, camino.solucion + "1"))
            cola.insertar(Camino(camino.n - 2, camino.solucion + "2"))


if __name__ == "__main__":
    cola = Cola_Encadenada()
    cola.insertar(Camino(4))
    obtener_caminos(cola)
