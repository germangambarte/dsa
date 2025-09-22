import random

from colas.encadenada import Cola_Encadenada


def mostrar(cola):
    a = cola.obtener_cola()
    i = 9
    while i >= 0:
        print(f"    {0 if a[i] is None else a[i]}")
        i -= 1

    print("[impresora]")
    print("\n")


class Impresora(Cola_Encadenada):
    __tiempo_de_trabajo: int
    __trabajando: int

    def __init__(self, tiempo_de_trabajo) -> None:
        super().__init__()
        self.__tiempo_de_trabajo = tiempo_de_trabajo
        self.__trabajando = 0

    def libre(self):
        return self.__trabajando == 0

    def liberar(self):
        self.__trabajando = 0

    def continuar_trabajando(self):
        self.__trabajando -= 1

    def comenzar_trabajo(self):
        self.__trabajando = self.__tiempo_de_trabajo


class Trabajo:
    paginas: int
    espera: int

    def __init__(self, espera, paginas=0):
        self.paginas = paginas if paginas != 0 else random.randint(1, 100)
        self.espera = espera


if __name__ == "__main__":
    impresora = Impresora(3)
    trabajo_en_proceso = Trabajo(0)
    duracion_total = 60

    trabajos_impresos = 0
    espera_total = 0

    for reloj in range(duracion_total):
        if reloj % 5 == 0:
            impresora.insertar(Trabajo(reloj))

        if trabajo_en_proceso.paginas <= 0:
            impresora.liberar()

        if impresora.libre():
            if trabajo_en_proceso.paginas > 0:
                impresora.insertar(trabajo_en_proceso)
            else:
                trabajos_impresos += 1
                espera_total += reloj - trabajo_en_proceso.espera
            trabajo_en_proceso = impresora.eliminar() or Trabajo(0, 0)
            impresora.comenzar_trabajo()
        else:
            trabajo_en_proceso.paginas -= 10
            impresora.continuar_trabajando()

    if trabajo_en_proceso.paginas > 0:
        impresora.insertar(trabajo_en_proceso)

    print(f"Cantidad de trabajos sin atender: {impresora.obtener_cantidad()}")
    print(f"Promedio de espera: {espera_total / trabajos_impresos:.2f}")
