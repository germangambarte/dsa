import numpy as np

# Construya un algoritmo que permita chequear la correcta aparición de paréntesis en una expresión
# aritmética, teniendo en cuenta que el primer paréntesis abierto es el último en ser cerrado.
# a) Elija el TAD apropiado, y construya el objeto de datos.
# b) Especifique e implemente la operación Suprimir_elem().


class Pila:
    __pila: np.ndarray
    __ultimo: int
    __capacidad: int
    __longitud: int

    def __init__(self, capacidad) -> None:
        self.__capacidad = capacidad
        self.__ultimo = 0
        self.__longitud = 0

    def insertar(self, item: str):
        pass

    def eliminar(self):
        pass

    def recorrer(self):
        pass

    def vacia(self):
        pass


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
            if resultado != ")":
                error = True
        i += 1
    if error == True:
        print("Ocurrió un problema")
    else:
        print("La expreción es correcta")
