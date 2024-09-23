import numpy as np


class PilaSecuencial:
    __items: np.ndarray
    __cantidad: int
    __tope: int
    __dimension: int

    def __init__(self, dim=0) -> None:
        self.__dimension = dim
        self.__tope = -1
        self.__cantidad = 0
        self.__items = np.empty(dim)

    def insertar(self, item: int) -> int:
        if self.__cantidad < self.__dimension:
            self.__tope += 1
            self.__items[self.__tope] = item
            self.__cantidad += 1
            return item
        else:
            print("Pila llena.\n")
            return 0

    def suprimir(self) -> int:
        if self.vacio():
            print("Pila vacio.\n")
            return 0
        else:
            eliminado = self.__items[self.__tope]
            self.__tope -= 1
            return eliminado

    def recorrer(self):
        for i in range(self.__tope, -1, -1):
            print(int(self.__items[i]), end=" ")
        print("\n")

    def vacio(self) -> bool:
        return self.__cantidad == 0


def mostrar_estado(p1, p2, p3):
    print("Estado de las pilas")
    print("Pila 1: ")
    p1.recorrer()
    print("Pila 2: ")
    p2.recorrer()
    print("Pila 3: ")
    p3.recorrer()


def verificar_movimiento(pila_o, pila_d):
    valido = True
    contenido_o = pila_o.suprimir()
    if pila_d.vacio():
        pila_d.insertar(contenido_o)
    else:
        contenido_d = pila_d.suprimir()
        pila_d.insertar(contenido_d)

        if contenido_o < contenido_d:
            pila_d.insertar(contenido_o)
        else:
            pila_o.insertar(contenido_o)
            valido = False
    return valido


def movimiento(p1, p2, p3):
    validez = True
    opciones = [1, 2, 3]
    print("Movimiento".center(100))

    origen = int(input("Ingresa el origen (1,2,3): "))
    opciones.remove(origen)
    destino = int(input(f"Ingresa el destino {opciones}: "))

    if (origen in (1, 2, 3)) and (destino in opciones):
        if origen == 1:
            if destino == 2:
                validez = verificar_movimiento(p1, p2)
            elif destino == 3:
                validez = verificar_movimiento(p1, p3)
        elif origen == 2:
            if destino == 1:
                validez = verificar_movimiento(p2, p1)
            elif destino == 3:
                validez = verificar_movimiento(p2, p3)
        elif origen == 3:
            if destino == 1:
                validez = verificar_movimiento(p3, p1)
            elif destino == 2:
                validez = verificar_movimiento(p3, p2)
    else:
        print("El origen y/o destino no son validos")
        validez = False

    if validez is False:
        print("El movimiento no es valido")

    return validez


if __name__ == "__main__":
    pila1 = PilaSecuencial(3)
    pila2 = PilaSecuencial(3)
    pila3 = PilaSecuencial(4)

    n = int(input("Ingresa la cantidad de discos: "))
    num_discos = n
    while n > 0:
        pila1.insertar(n)
        n -= 1

    mostrar_estado(pila1, pila2, pila3)
    cont_movimientos = 0
    while (pila1.vacio() is False) or (pila2.vacio() is False):
        if movimiento(pila1, pila2, pila3):
            print("Movimiento exitoso")
            cont_movimientos += 1
        mostrar_estado(pila1, pila2, pila3)
    print(f"El juego se completo con {cont_movimientos} movimientos")
    print(
        "La cantidad minima de movimientos necesarios para completarlo es: ",
        pow(2, num_discos) - 1,
    )

    """Sugerencia de Movimientos O,D
    1,2
    1,3
    2,3
    1,2
    3,1
    3,2
    1,2
    1,3
    2,3
    2,1
    3,1
    2,3
    1,2
    1,3
    2,3
    """


# if __name__ == "__main__":
#     pila = PilaSecuencial(4)
#
#     pila.insertar(1)
#     pila.insertar(2)
#     pila.insertar(3)
#     pila.insertar(4)
#
#     pila.recorrer()
#
#     pila.suprimir()
#     pila.suprimir()
#
#     pila.recorrer()
