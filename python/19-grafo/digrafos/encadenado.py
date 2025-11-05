import math
from grafos.encadenado import Grafo

class Digrafo(Grafo):
    def __init__(self, n: int) -> None:
        super().__init__(n)

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

    def grado_salida(self,u:int):
        grado = 0
        actual = self._matriz[u].get_cabeza()
        while actual is not None:
            grado +=1
            actual = actual.get_siguiente()
        return grado

    def pozo(self,u):
        return self.grado_salida(u) == 0

    def grado_entrada(self,u:int):
        grado = 0
        for i in range(self._n):
            if self._matriz[i].recuperar(u) is not None:
                grado +=1
        return grado

    def fuente(self,u):
        return self.grado_entrada(u) == 0

if __name__ == "__main__":
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

