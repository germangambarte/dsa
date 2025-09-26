from random import randint, random

from colas.secuencial import Cola_Secuencial


def mostrar(cola):
    a = cola.obtener_cola()
    i = 9
    while i >= 0:
        print(f"    {0 if a[i] is None else a[i]}")
        i -= 1

    print("[impresora]")
    print("\n")


class Trabajo:
    paginas: int
    espera: int

    def __init__(self, espera):
        self.paginas = randint(1, 100)
        self.espera = espera


if __name__ == "__main__":
    impresora = Cola_Secuencial(100)
    duracion_total = 60
    trabajos_impresos = 0
    espera_total = 0
    llegada = 5
    tiempo_de_trabajo = 3
    trabajando = 0
    reloj = 0
    paginas =10
    procesando = None

    while reloj <= duracion_total:
        if random() <= 1 / llegada:
            impresora.insertar(Trabajo(reloj))

        while paginas > 0




    print(f"Cantidad de trabajos sin atender: {impresora.obtener_cantidad()}")
    print(f"Promedio de espera: {espera_total / trabajos_impresos:.2f}")
