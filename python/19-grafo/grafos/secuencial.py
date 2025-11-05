import math

import numpy as np
from cola import Cola
from pila import Pila


class Grafo:
    _n: int
    _matriz: np.ndarray
    _tiempo: int

    def __init__(self, n: int) -> None:
        self._n = n
        self._matriz = np.zeros((n, n), dtype=float)
        self._tiempo = 0

    def insertar_arista(self, nodo_a: int, nodo_b: int, peso=1) -> None:
        self._matriz[nodo_a, nodo_b] = peso

    """OBTENER ADYACENTES"""

    def adyacentes(self, nodo):
        ady = np.zeros(self._n, dtype=int)
        for i in range(self._n):
            if self._matriz[nodo, i] > 0:
                ady[i] = 1
        return ady

    """BUSQUEDA EN AMPLITUD"""

    def bea(self, s: int):
        d = np.full(self._n, math.inf)
        cola = Cola(self._n)
        d[s] = 0
        cola.insertar(s)
        while not cola.vacia():
            v = cola.eliminar()
            for i in range(self._n):
                if self._matriz[v, i] > 0 and d[i] == math.inf:
                    d[i] = d[v] + 1
                    cola.insertar(i)
        return d

    """BUSQUEDA EN PROFUNDIDAD"""

    def bep(self):
        self._tiempo = 0
        d = np.zeros(self._n, dtype=int)  # tiempos de descubirmiento
        f = np.zeros(self._n, dtype=int)  # tiempos de finalización

        for s in range(self._n):
            if d[s] == 0:
                self.bep_visita(d, f, s)
        print(f"BEP: {d}")

    def bep_visita(self, d, f, s):
        self._tiempo += 1
        d[s] = self._tiempo

        for u in range(self._n):
            if self._matriz[s, u] > 0 and d[u] == 0:
                self.bep_visita(d, f, u)
        self._tiempo += 1
        f[s] = self._tiempo

    def mostrar(self):
        print("  ", end=" ")
        for i in range(self._n):
            print(f"  [{i}]", end=" ")
        print()
        for i in range(self._n):
            print(f"[{i}]", end=" ")
            for j in range(self._n):
                print(f" {self._matriz[i, j]} ", end=" ")
            print()

    def __distancia_minima(self, c, d):
        min = math.inf
        u = None

        for i in range(self._n):
            if not c[i] and d[i] < min:
                min = d[i]
                u = i
        return u

    """OBTENER CAMINO MÁS CORTO"""

    def dijkstra(self, origen):
        conocido = np.zeros(self._n, dtype=bool)
        distancia = np.full(self._n, math.inf)
        predecesores = np.full(self._n, -1, dtype=int)

        distancia[origen] = 0

        for _ in range(self._n):
            u = self.__distancia_minima(conocido, distancia)
            if u is not None:
                conocido[u] = True
                for v in range(self._n):
                    peso = self._matriz[u, v]
                    if peso > 0 and not conocido[v]:
                        dist = distancia[u] + peso
                        if dist < distancia[v]:
                            distancia[v] = dist
                            predecesores[v] = u

        return distancia, predecesores

    def camino_mas_corto(self, origen, destino):
        distancia, predecesores = self.dijkstra(origen)
        if distancia[destino] == math.inf:
            print("No existe camino")
            return None

        camino = Pila(self._n)
        actual = destino
        while actual != -1:
            camino.insertar(actual)
            actual = predecesores[actual]
        print("camino:", end=" ")
        camino.mostrar()

    """VERIFICAR SI EXISTE CONEXIDAD"""

    def bea_no_dirigido(self, s: int):
        d = np.full(self._n, math.inf)
        cola = Cola(self._n)
        d[s] = 0
        cola.insertar(s)
        while not cola.vacia():
            v = cola.eliminar()
            for i in range(self._n):
                if (self._matriz[v, i] > 0 or self._matriz[i, v] > 0) and d[
                    i
                ] == math.inf:
                    d[i] = d[v] + 1
                    cola.insertar(i)
        return d

    def conexo(self):
        d = self.bea_no_dirigido(0)
        if math.inf not in d:
            print("grafo conexo")
        else:
            print("grafo no conexo")

    """OBTENER TIPO DE CONEXIDAD"""

    def tipo_de_conexidad(self):
        hay_camino = True
        i = 0
        while i < self._n and hay_camino:
            bea = self.bea(i)
            if math.inf in bea:
                hay_camino = False
            else:
                i += 1

        if hay_camino:
            print("digrafo fuertemente conexo")
        else:
            print("digrafo simple conexo")

    """CHEQUEAR SI ES ACÍCLICO"""

    def __aciclico_visita(self, d, f, s):
        self._tiempo += 1
        d[s] = self._tiempo

        for u in range(self._n):
            if self._matriz[s, u] > 0:
                if d[u] == 0 and self.__aciclico_visita(d, f, u):
                    return True
                elif f[u] == 0:
                    return True
        self._tiempo += 1
        f[s] = self._tiempo
        return False

    def aciclico(self):
        self._tiempo = 0
        d = np.zeros(self._n, dtype=int)
        f = np.zeros(self._n, dtype=int)
        hay_ciclo = False

        s = 0
        while s < self._n and not hay_ciclo:
            if d[s] == 0:
                if self.__aciclico_visita(d, f, s):
                    hay_ciclo = True
            s += 1

        if hay_ciclo:
            print("El grafo no es acíclico.")
        else:
            print("El grafo es acíclico.")

if __name__ == "__main__":
    print("--- PRUEBA CON GRAFO CÍCLICO Y CONEXO ---")
    aristas = [
        (0, 1, 5),
        (0, 4, 2),
        (1, 0, 5),
        (1, 3, 3),
        (1, 4, 1),
        (2, 3, 4),
        (2, 4, 6),
        (3, 1, 3),
        (3, 2, 4),
        (4, 0, 2),
        (4, 1, 1),
        (4, 2, 6),
    ]

    grafo = Grafo(5)
    for fila, col, peso in aristas:
        grafo.insertar_arista(fila, col, peso)

    grafo.mostrar()

    # Pruebas con el grafo:
    grafo.bea(0)
    grafo.bep()
    grafo.camino_mas_corto(0, 3)
    grafo.conexo()
    grafo.aciclico()

    print("\n--- PRUEBA CON GRAFO NO CONEXO Y ACÍCLICO ---")
    grafo_aciclico = Grafo(4)
    grafo_aciclico.insertar_arista(0, 1)
    grafo_aciclico.insertar_arista(2, 3)  # Dos componentes desconectados (0-1) y (2-3)
    grafo_aciclico.mostrar()
    grafo.conexo()
    grafo_aciclico.aciclico()
