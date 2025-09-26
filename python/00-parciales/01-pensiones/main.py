import random

# Ejercicio 2: encontrar TAD adecuado
# - simular durante 5 horas
# - dos cajeros
# - tiempo de atención: 6 y 4 minutos
# - frecuencia de llegada de pensionados: 3 minutos


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
    __cab: Nodo | None
    __cola: Nodo | None
    __long: int

    def __init__(self) -> None:
        self.__cab = None
        self.__cola = None
        self.__long = 0

    def insertar(self, item):
        nuevo_nodo = Nodo(item)

        if self.vacia():
            self.__cab = nuevo_nodo
        else:
            self.__cola.set_siguiente(nuevo_nodo)
        self.__cola = nuevo_nodo
        self.__long += 1

    def eliminar(self):
        if self.vacia():
            return None
        temp = self.__cab
        self.__cab = temp.get_siguiente()
        self.__long -= 1
        return temp.get_item()

    def recorrer(self):
        actual = self.__cab
        while actual:
            print(actual.get_item(), end=" ")
            actual = actual.get_siguiente()

    def vacia(self):
        return self.__long == 0


if __name__ == "__main__":
    cajeros = [Cola(), Cola()]
    tiempo_atencion = [6, 4]
    antendidos = [0, 0]
    tiempo_llegada = 3
    n = 2

    for reloj in range(300):
        if reloj % 3 == 0:
            cajeros[random.randint(0, n - 1)].insertar(1)
        i = 0
        while i < n:
            if reloj % tiempo_atencion[i] and not cajeros[i].vacia():
                cajeros[i].eliminar()
                antendidos[i] += 1
            i += 1

    print(f"Cajero 1 atendio: {antendidos[0]} pensionados.")
    print(f"Cajero 2 atendio: {antendidos[1]} pensionados.")
