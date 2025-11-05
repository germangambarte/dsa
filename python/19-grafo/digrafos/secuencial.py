from grafos.secuencial import Grafo

class Digrafo(Grafo):
    def __init__(self, n: int) -> None:
        super().__init__(n)

    """OPERACIONES ESPEDIFICAS DE LOS DIGRAFOS"""

    def grado_salida(self, u: int) -> int:
        grado = 0
        for i in range(self._n):
            if self._matriz[u, i] > 0:
                grado += 1
        return grado

    def grado_entrada(self, u: int) -> int:
        grado = 0
        for i in range(self._n):
            if self._matriz[i, u] > 0:
                grado += 1
        return grado

    def fuente(self, u):
        return self.grado_entrada(u) == 0

    def pozo(self, u):
        return self.grado_salida(u) == 0


if __name__ == "__main__":
    print("--- MATRIZ ---")
    fuente_pozo = [
        (0, 1, 5),
        (0, 4, 2),
        (1, 3, 3),
        (3, 2, 4),
        (4, 2, 1),
    ]

    simple_conexo = [
        (0, 1, 5),
        (1, 2, 3),
        (2, 3, 4),
        (3, 1, 2),  # ciclo 1->2->3->1
        (2, 4, 6),  # 4 es alcanzable desde el ciclo, pero no hay aristas de regreso a 0
    ]

    fuertemente_conexo = [
        (0, 1, 5),
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 2),
        (4, 0, 1),  # ciclo 0->1->2->3->4->0 asegura fuerte conexidad
        # opcional (no necesario): (0,2,2), (3,1,2) para hacer rutas más directas
    ]

    digrafo = Digrafo(5)
    for fila, col, peso in simple_conexo:
        digrafo.insertar_arista(fila, col, peso)

    digrafo.mostrar()

    # Pruebas con el grafo:
    digrafo.bea(0)
    digrafo.bep()
    digrafo.camino_mas_corto(0, 2)
    digrafo.conexo()
    digrafo.aciclico()
    fuente = 0
    print(f"nodo {fuente} es fuente") if digrafo.fuente(fuente) else print(
        f"nodo {fuente} no es fuente"
    )
    pozo = 2
    print(f"nodo {pozo} es pozo") if digrafo.pozo(pozo) else print(
        f"nodo {pozo} no es pozo"
    )
    digrafo.tipo_de_conexidad()

