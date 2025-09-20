import random
from lista_secuencial import Lista

random.seed()


class Matriz(Lista):
    def __init__(self, filas: int, columnas: int) -> None:
        super().__init__(filas, columnas)

    def inicializar(self):
        for fila in range(self.get_filas()):
            for col in range(self.get_columnas()):
                self.insertar(fila + 1, col + 1, self.__crear_componente())

    def __crear_componente(self):
        return 1 if random.random() < 0.2 else 0

    def suma(self, m):
        resultado = Matriz(self.get_filas(), self.get_columnas())
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                celda1 = self.recuperar(i + 1, j + 1)
                celda2 = m.recuperar(i + 1, j + 1)
                resultado.insertar(i + 1, j + 1, celda1 + celda2)
        return resultado


if __name__ == "__main__":
    lista = Matriz(3, 3)
    lista2 = Matriz(3, 3)

    lista.inicializar()
    lista.recorrer()
    print()
    lista2.inicializar()
    lista2.recorrer()
    print()
    resultado = lista.suma(lista2)
    resultado.recorrer()
