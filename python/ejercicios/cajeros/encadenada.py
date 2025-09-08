import numpy as np

from colas.encadenada import Cola_Encadenada



def buscar_cola_vacia(cajeros):
    i = 0
    while i < len(cajeros):
        if cajeros[i].vacia():
            return i
        i += 1
    return -1


def buscar_cola_mas_corta(cajeros):
    i = 0
    min, min_i = 9999, -1
    while i < len(cajeros):
        cantidad_clientes = cajeros[i].obtener_cantidad()
        if cantidad_clientes < min:
            min = cantidad_clientes
            min_i = i
        i += 1
    return min_i


class Cajero(Cola_Encadenada):
    __tiempo_de_trabajo: int
    __trabajando: int

    def __init__(self, tiempo_de_trabajo: int):
        super().__init__()
        self.__tiempo_de_trabajo = tiempo_de_trabajo
        self.__trabajando = 0

    def libre(self):
        return self.__trabajando == 0

    def comenzar_trabajo(self):
        self.__trabajando = self.__tiempo_de_trabajo

    def continuar_trabajando(self):
        self.__trabajando -= 1


if __name__ == "__main__":
    duracion = 120
    cajeros = np.array([Cajero(5), Cajero(3), Cajero(4)])
    espera_maxima = 0
    atendidos = {"contador": 0, "espera": 0}
    no_atendidos = {"contador": 0, "espera": 0}

    for reloj in range(duracion):
        if reloj % 2 == 0:
            vacia = buscar_cola_vacia(cajeros)
            if vacia == -1:
                mas_corta = buscar_cola_mas_corta(cajeros)
                cajeros[mas_corta].insertar(reloj)
            else:
                cajeros[vacia].insertar(reloj)

        i = 0
        while i < len(cajeros) and not cajeros[i].vacia():
            if cajeros[i].libre():
                espera = reloj - cajeros[i].eliminar()
                atendidos["contador"] += 1
                atendidos["espera"] += espera
                if espera > espera_maxima:
                    espera_maxima = espera
                cajeros[i].comenzar_trabajo()
            else:
                cajeros[i].continuar_trabajando()
            i += 1
    for cajero in cajeros:
        while not cajero.vacia():
            no_atendidos["espera"] += cajero.eliminar()
            no_atendidos["contador"] += 1

    print(f"Tiempo maximo de espera: {espera_maxima}")
    print(f"Cantidad de clientes atendidos: {atendidos['contador']}")
    print(f"Cantidad de clientes no atendidos: {no_atendidos['contador']}")
    print(
        f"Promedio de espera de clientes atendidos: {atendidos['espera'] / atendidos['contador']}"
    )
    print(
        f"Cantidad de espera de clientes no atendidos: {no_atendidos['espera'] / no_atendidos['contador']}"
    )
