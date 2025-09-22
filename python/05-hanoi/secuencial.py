import numpy as np
from pilas.secuencial import Pila_Secuencial


class Hanoi:
    __n: int
    __movimientos: int
    __movimientos_minimos: int
    __torres: np.ndarray

    def __init__(self, n) -> None:
        self.__n = n
        self.__movimientos = 0
        self.__movimientos_minimos = 2**self.__n - 1
        self.__torres = np.array(
            [Pila_Secuencial(n), Pila_Secuencial(n), Pila_Secuencial(n)]
        )
        for i in range(n, 0, -1):
            self.__torres[-1].insertar(i)

    def intentar_movimiento(self, nro_pila_origen: int, nro_pila_destino: int):
        if 0 >= nro_pila_origen > self.__n or 0 >= nro_pila_destino > self.__n:
            print(f"nro de pila no válido. debe ser un número entre 1 y {self.__n}")
        pila_origen = self.__torres[nro_pila_origen - 1]
        pila_destino = self.__torres[nro_pila_destino - 1]

        if pila_origen.vacia():
            print(
                f"[movimiento {self.__movimientos + 1}] No hay piezas en la pila de origen"
            )
            return
        if pila_destino.vacia():
            self.__movimientos += 1
            pila_destino.insertar(pila_origen.eliminar())
            return

        ultimo_item_origen = pila_origen.eliminar()
        ultimo_item_destino = pila_destino.eliminar()

        if ultimo_item_origen > ultimo_item_destino:
            pila_origen.insertar(ultimo_item_origen)
            pila_destino.insertar(ultimo_item_destino)
            print(
                f"[movimiento {self.__movimientos + 1}] movimiento no válido. la pieza {ultimo_item_origen} > {ultimo_item_destino}."
            )
            return

        pila_destino.insertar(ultimo_item_destino)
        pila_destino.insertar(ultimo_item_origen)
        self.__movimientos += 1

    def mostrar(self):
        print(f"lleva {self.__movimientos} movimiento/s")
        print()
        self.__torres[0].mostrar()
        print(" [1]")
        self.__torres[1].mostrar()
        print(" [2]")
        self.__torres[2].mostrar()
        print(" [3]")
        print()

    def finalizo(self):
        return self.__torres[1].vacia() and self.__torres[2].vacia()

    def mostrar_resultados(self):
        print("Juego Terminado!")
        print(f"cantidad de movimientos: {self.__movimientos}")
        print(f"cantidad mínima de movimientos: {self.__movimientos_minimos}")


if __name__ == "__main__":
    hanoi = Hanoi(3)

    hanoi.mostrar()

    nro_pila_origen = int(input("\norigen (0 para finalizar): "))
    while nro_pila_origen != 0:
        nro_pila_destino = int(input("destino: "))

        hanoi.intentar_movimiento(nro_pila_origen, nro_pila_destino)
        hanoi.mostrar()

        if hanoi.finalizo():
            hanoi.mostrar_resultados()
            break

        nro_pila_origen = int(input("origen (0 para finalizar): "))
