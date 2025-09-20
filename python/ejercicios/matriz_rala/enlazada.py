import random

from lista_enlazada import Celda, Lista

random.seed()


class Matriz(Lista):
    __filas: int
    __columnas: int

    def __init__(self, filas, columnas) -> None:
        super().__init__()
        self.__filas = filas
        self.__columnas = columnas

    def inicializar(self):
        posicion = 1
        for fila in range(self.__filas):
            for col in range(self.__columnas):
                self.insertar(posicion, Celda(self.__crear_componente(), fila, col))
                posicion += 1

    def __crear_componente(self):
        return 1 if random.random() < 0.2 else 0

    def get_dimension(self):
        return self.__filas, self.__columnas

    def suma(self, m2):
        resultado = Matriz(self.__filas, self.__columnas)
        posicion = 1
        while posicion <= self.get_longitud():
            celda1 = self.recuperar(posicion)
            celda2 = m2.recuperar(posicion)
            resultado.insertar(
                posicion,
                Celda(
                    celda1.get_componente() + celda2.get_componente(),
                    celda1.get_fila(),
                    celda1.get_columna(),
                ),
            )
            posicion += 1
        return resultado
        return resultado


if __name__ == "__main__":
    lista1 = Matriz(3, 3)
    lista2 = Matriz(3, 3)
    lista1.inicializar()
    lista2.inicializar()
    lista1.recorrer()
    print("+")
    lista2.recorrer()

    resultado = lista1.suma(lista2)
    resultado.recorrer()
