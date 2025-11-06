import math

import numpy as np
from utils.cola import Cola
from utils.lista import Lista
from utils.pila import Pila


class Nodo:
    __nodo: int
    __peso: float

    def __init__(self, nodo: int, peso: float):
        self.__nodo = nodo
        self.__peso = peso

    def get_nodo(self):
        return self.__nodo

    def get_peso(self):
        return self.__peso


class Grafo:
    _n: int
    _matriz: np.ndarray
    _tiempo: int

    def __init__(self, n: int) -> None:
        self._n = n
        self._matriz = np.zeros(n, dtype=Lista)
        self._tiempo = 0

    def inicializar(self):
        for i in range(self._n):
            self._matriz[i] = Lista()

    def insertar_arista(self, nodo_a: int, nodo_b: int, peso=1) -> None:
        self._matriz[nodo_a].insertar(Nodo(nodo_b, peso))

    """OBTENER ADYACENTES"""

    def adyacentes(self, nodo):
        return self._matriz[nodo]

    """BUSQUEDA EN AMPLITUD"""

    def bea(self, s: int):
        d = np.full(self._n, -1)
        d_index = 0
        f = np.full(self._n, math.inf)

        cola = Cola(self._n)
        f[s] = 0
        d[d_index] = s
        d_index = 1
        cola.insertar(s)
        while not cola.vacia():
            v = cola.eliminar()
            for i in range(self._n):
                existe = self._matriz[v].buscar(i)
                if existe is not None and f[i] == math.inf:
                    f[i] = f[v] + 1
                    d[d_index] = i
                    d_index += 1
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
        return d

    def bep_visita(self, d, f, s):
        self._tiempo += 1
        d[s] = self._tiempo

        for u in range(self._n):
            adyacente = self._matriz[s].buscar(u)
            if adyacente is not None:
                if d[u] == 0:
                    self.bep_visita(d, f, u)
                    return True
                elif f[u] == 0:
                    return True
        self._tiempo += 1
        f[s] = self._tiempo
        return False

    def mostrar(self):
        for i in range(self._n):
            print(f"[{i}]", end=" ")
            self._matriz[i].recorrer()
        print()

    """CAMINO MÁS CORTO"""

    def __distancia_minima(self, c, d):
        min = math.inf
        u = None

        for i in range(self._n):
            if not c[i] and d[i] < min:
                min = d[i]
                u = i
        return u

    def dijkstra(self, origen):
        conocido = np.zeros(self._n, dtype=bool)
        distancia = np.full(self._n, math.inf)
        predecesores = np.full(self._n, -1, dtype=int)

        distancia[origen] = 0

        for _ in range(self._n):
            u = self.__distancia_minima(conocido, distancia)
            if u is not None:
                conocido[u] = True
                actual = self._matriz[u].get_cabeza()
                while actual is not None:
                    arista = actual.get_item()
                    v = arista.get_nodo()
                    if not conocido[v]:
                        dist = distancia[u] + arista.get_peso()
                        if dist < distancia[v]:
                            distancia[v] = dist
                            predecesores[v] = u
                    actual = actual.get_siguiente()

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

    """CONEXIDAD"""

    def bea_no_dirigido(self, s: int):
        d = np.full(self._n, -1)
        cola = Cola(self._n)
        d[s] = 0
        cola.insertar(s)
        while not cola.vacia():
            v = cola.eliminar()
            for i in range(self._n):
                hay_arista = (
                    self._matriz[v].buscar(i) is not None
                    or self._matriz[i].buscar(v) is not None
                )
                if hay_arista and d[i] == -1:
                    d[i] = d[v] + 1
                    cola.insertar(i)
        return d

    def conexo(self):
        resultado = self.bea_no_dirigido(0)
        if -1 not in resultado:
            print("grafo conexo")
        else:
            print("grafo no conexo")

    """VERIFICAR SI ES ACÍCLICO"""

    def __aciclico_visita(self, d, f, s):
        self._tiempo += 1
        d[s] = self._tiempo

        for u in range(self._n):
            existe = self._matriz[s].buscar(u)
            if existe is not None:
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
    grafo.inicializar()
    for fila, col, peso in aristas:
        grafo.insertar_arista(fila, col, peso)

    grafo.mostrar()

    d = grafo.bea(0)
    print(f"BEA: {d}")
    d = grafo.bep()
    print(f"BEP: {d}")
    grafo.camino_mas_corto(0, 3)
    grafo.conexo()
    grafo.aciclico()

    print("\n--- PRUEBA CON GRAFO NO CONEXO Y ACÍCLICO ---")
    grafo_aciclico = Grafo(4)
    grafo_aciclico.inicializar()
    grafo_aciclico.insertar_arista(0, 1)
    grafo_aciclico.insertar_arista(2, 3)  # Dos componentes desconectados (0-1) y (2-3)
    grafo_aciclico.mostrar()
    grafo.conexo()
    grafo_aciclico.aciclico()
