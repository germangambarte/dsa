from colas.secuencial import Cola_Secuencial


class Camino:
    n: int
    solucion: str

    def __init__(self, n, solucion="") -> None:
        self.n = n
        self.solucion = solucion


def obtener_caminos(cola: Cola_Secuencial):
    while not cola.vacia():
        camino = cola.eliminar() or Camino(0, "")
        if camino.n == 0:
            print(camino.solucion)
        elif camino.n == 1:
            cola.insertar(Camino(camino.n - 1, camino.solucion + "1"))
        else:
            cola.insertar(Camino(camino.n - 1, camino.solucion + "1"))
            cola.insertar(Camino(camino.n - 2, camino.solucion + "2"))


if __name__ == "__main__":
    cola = Cola_Secuencial(10)
    cola.insertar(Camino(4))
    obtener_caminos(cola)
