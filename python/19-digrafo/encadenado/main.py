import math

import numpy as np
from cola import Cola
from lista import Lista
from pila import Pila


class Arista:
    __nodo: int
    __peso: float

    def __init__(self, nodo: int, peso: float):
        self.__nodo = nodo
        self.__peso = peso

    def get_nodo(self):
        return self.__nodo

    def get_peso(self):
        return self.__peso


class Digrafo:
    __n: int
    __matriz: np.ndarray
    __tiempo: int

    def __init__(self, n: int) -> None:
        self.__n = n
        self.__matriz = np.zeros(n, dtype=Lista)
        self.__tiempo = 0

    def inicializar(self):
        for i in range(self.__n):
            self.__matriz[i] = Lista()

    def insertar_arista(self, nodo_a: int, nodo_b: int, peso=1) -> None:
        self.__matriz[nodo_a].insertar(Arista(nodo_b, peso))

    def adyacentes(self, nodo):
        return self.__matriz[nodo]

    def bea(self, s: int):
        d = np.full(self.__n, math.inf)
        cola = Cola(self.__n)
        d[s] = 0
        cola.insertar(s)
        while not cola.vacia():
            v = cola.eliminar()
            for i in range(self.__n):
                existe = self.__matriz[v].buscar(i)
                if existe is not None and d[i] == math.inf:
                    d[i] = d[v] + 1
                    cola.insertar(i)
        print(f"BEA: {d}")

    def bep(self):
        self.__tiempo = 0
        d = np.zeros(self.__n, dtype=int)  # tiempos de descubirmiento
        f = np.zeros(self.__n, dtype=int)  # tiempos de finalización

        for s in range(self.__n):
            if d[s] == 0:
                self.bep_visita(d, f, s)
        print(f"BEP: {d}")

    def bep_visita(self, d, f, s):
        self.__tiempo += 1
        d[s] = self.__tiempo

        for u in range(self.__n):
            adyacente = self.__matriz[s].buscar(u)
            if adyacente is not None:
                if d[u] == 0:
                    self.bep_visita(d, f, u)
                    return True
                elif f[u] == 0:
                    return True
        self.__tiempo += 1
        f[s] = self.__tiempo
        return False

    def mostrar(self):
        for i in range(self.__n):
            print(f"[{i}]", end=" ")
            self.__matriz[i].recorrer()
        print()

    def __distancia_minima(self, c, d):
        min = math.inf
        u = None

        for i in range(self.__n):
            if not c[i] and d[i] < min:
                min = d[i]
                u = i
        return u

    def dijkstra(self, origen):
        conocido = np.zeros(self.__n, dtype=bool)
        distancia = np.full(self.__n, math.inf)
        predecesores = np.full(self.__n, -1, dtype=int)

        distancia[origen] = 0

        for _ in range(self.__n):
            u = self.__distancia_minima(conocido, distancia)
            if u is not None:
                conocido[u] = True

                actual = self.__matriz[u].get_cabeza()
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

        camino = Pila(self.__n)
        actual = destino
        while actual != -1:
            camino.insertar(actual)
            actual = predecesores[actual]
        print("camino:", end=" ")
        camino.mostrar()

    def conexo(self):
        d, _ = self.dijkstra(0)
        if math.inf in d:
            print("El grafo no es conexo")
        else:
            print("El grafo es conexo")

    def __aciclico_visita(self, d, f, s):
        self.__tiempo += 1
        d[s] = self.__tiempo

        for u in range(self.__n):
            existe = self.__matriz[s].buscar(u)
            if existe is not None:
                if d[u] == 0 and self.__aciclico_visita(d, f, u):
                    return True
                elif f[u] == 0:
                    return True
        self.__tiempo += 1
        f[s] = self.__tiempo
        return False

    def aciclico(self):
        self.__tiempo = 0
        d = np.zeros(self.__n, dtype=int)
        f = np.zeros(self.__n, dtype=int)
        hay_ciclo = False

        s = 0
        while s < self.__n and not hay_ciclo:
            if d[s] == 0:
                if self.__aciclico_visita(d, f, s):
                    hay_ciclo = True
            s += 1

        if hay_ciclo:
            print("El grafo no es acíclico (es cíclico).")
        else:
            print("El grafo es acíclico.")

    def grado_salida(self,u:int):
        grado = 0
        actual = self.__matriz[u].get_cabeza()
        while actual is not None:
            grado +=1
            actual = actual.get_siguiente()
        return grado

    def pozo(self,u):
        return self.grado_salida(u) == 0

    def grado_entrada(self,u:int):
        grado = 0
        for i in range(self.__n):
            if self.__matriz[i].recuperar(u) is not None:
                grado +=1
        return grado

    def fuente(self,u):
        return self.grado_entrada(u) == 0

if __name__ == "__main__":
    print("--- ARREGLO DE LISTAS ---")
    print("--- PRUEBA CON DIGRAFO CÍCLICO Y CONEXO ---")

    aristas = [
        (0, 1, 5),
        (0, 4, 2),
        (1, 3, 3),
        # (2, 4, 6),
        # (2, 0, 6),
        (3, 2, 4),
        (4, 1, 1),
    ]

    digrafo = Digrafo(5)
    digrafo.inicializar()
    for fila, col, peso in aristas:
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
