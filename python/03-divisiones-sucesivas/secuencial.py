from pilas.secuencial import Pila_Secuencial


def divisiones_sucesivas_secuencial(pila: Pila_Secuencial, num: int):
    if num < 2:
        pila.insertar(1)
        return
    pila.insertar(num % 2)
    divisiones_sucesivas_secuencial(pila, int(num / 2))


if __name__ == "__main__":
    pila = Pila_Secuencial(10)
    divisiones_sucesivas_secuencial(pila, 100)
    pila.mostrar()
