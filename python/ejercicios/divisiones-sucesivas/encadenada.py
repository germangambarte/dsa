from pilas.encadenada import Pila_Encadenada


def divisiones_sucesivas_encadenada(pila: Pila_Encadenada, num: int):
    if num < 2:
        pila.insertar(1)
        return
    pila.insertar(num % 2)
    divisiones_sucesivas_encadenada(pila, int(num / 2))


if __name__ == "__main__":
    pila = Pila_Encadenada()
    divisiones_sucesivas_encadenada(pila, 100)
    pila.mostrar()
