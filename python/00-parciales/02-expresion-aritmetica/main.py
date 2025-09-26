import numpy as np

# Construya un algoritmo que permita chequear la correcta aparición de paréntesis en una expresión
# aritmética, teniendo en cuenta que el primer paréntesis abierto es el último en ser cerrado.
# a) Elija el TAD apropiado, y construya el objeto de datos.
# b) Especifique e implemente la operación Suprimir_elem().


class Pila:
    __pila: np.ndarray
    __cap: int
    __long: int

    def __init__(self, cap) -> None:
        self.__cap = cap
        self.__long = 0
        self.__pila = np.empty(cap, dtype=str)

    def insertar(self, item: str):
        if self.llena():
            print("pila llena.")
            return None
        self.__pila[self.__long] = item
        self.__long += 1

    def eliminar(self):
        if self.vacia():
            print("pila vacia.")
            return
        self.__long
        return self.__pila[self.__long]

    def recorrer(self):
        for i in range(self.__long):
            print(self.__pila[i], end=" ")
        print()

    def vacia(self):
        return self.__long == 0

    def llena(self):
        return self.__long == self.__cap


if __name__ == "__main__":
    pila = Pila(5)
    expresion = "(a+b) * (b-a)"
    i = 0
    error = False
    while i < len(expresion) and error is False:
        letra = expresion[i]
        if letra == "(":
            pila.insertar(letra)
        if letra == ")":
            resultado = pila.eliminar()
            print({"resultado": resultado})
            if resultado != "(":
                error = True
        i += 1
    if error:
        print("Ocurrió un problema")
    else:
        print("La expreción es correcta")
