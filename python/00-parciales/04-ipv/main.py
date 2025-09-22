# Ejercicio 2: Construya un algoritmo que, haciendo uso de un TAD adecuado, permita simular
# durande cinco horas, el comportamiento de inscripciones de viviendas en el IPV, teniendo
# en cuenta que el tiempo de atención del empleado es de 15 minutos, en promedio. Además,
# la frecuencia de llegada de los solicitantes es de 10 minutos.
#     a) Fundamente la elección de TAD usado para resolver la problemática planteada.
#     b) Construya el objeto de datos.
#     c) Implemente la operación suprimir()
#     d) Una vez finalizada la simulación, indique cuál fue el tiempo mácimo de cola de
#        espera de aquellos solicitantes que no fueron atendidos.


class Nodo:
    def __init__(self, item: int, sig=None) -> None:
        self.__item = item
        self.__sig = sig

    def get_item(self):
        return self.__item

    def get_siguiente(self):
        return self.__sig

    def set_siguiente(self, sig: "Nodo"):
        self.__sig = sig


class Cola:
    __cabeza: Nodo | None
    __cola: Nodo | None
    __cantidad: int

    def insertar(self, item):
        pass

    def eliminar(self):
        if self.vacia():
            return None

        temp = self.__cabeza

        self.__cabeza = temp.get_siguiente()
        self.__cantidad -= 1

        return temp.get_item()

    def recorrer(self):
        pass

    def vacia(self):
        pass


if __name__ == "__main__":
    cola = Cola()
    duracion = 300
    max = 0
    for reloj in range(duracion):
        if reloj % 10 == 0:
            cola.insertar(reloj)
        if reloj % 15 == 0:
            llegada = cola.eliminar()
            espera = reloj - llegada
            if espera > max:
                max = espera
    print(f"max = {max}")
