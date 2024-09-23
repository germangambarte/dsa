class Nodo:
    __item: "Impresion"
    __siguiente: "Nodo"

    def __init__(self, item=None, siguiente=None) -> None:
        self.__item = item
        self.__siguiente = siguiente

    def obtener_item(self):
        return self.__item

    def obtener_siguiente(self):
        return self.__siguiente

    def cargar_item(self, item):
        self.__item = item

    def cargar_siguiente(self, siguiente):
        self.__siguiente = siguiente

class ColaEncadenada:
    __cantidad: int
    __primero: Nodo
    __ultimo: Nodo

    def __init__(self) -> None:
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def insertar(self, item):
        nuevo_nodo = Nodo(item)
        if self.__ultimo is None:     
            # Si la cola está vacía 
            self.__primero = nuevo_nodo
        else:
            # Si la cola no está vacía
            self.__ultimo.cargar_siguiente(nuevo_nodo)

        self.__ultimo = nuevo_nodo
        self.__cantidad += 1
        return self.__ultimo.obtener_item()

    def suprimir(self):
        if self.vacia():
            print("Cola Vacia.\n")
            return None
        else:
            aux = Nodo(
                self.__primero.obtener_item(), self.__primero.obtener_siguiente()
            )
            self.__primero = self.__primero.obtener_siguiente()
            self.__cantidad -= 1
            if self.__primero is None:
                self.__ultimo = None
            return aux.obtener_item()

    def recuperar_primero(self):
        return self.__primero

    def recorrer(self):
        actual = self.__primero
        while actual != None:
            print(actual.obtener_item(), end=" ")
            actual = actual.obtener_siguiente()
        print("\n")

    def vacia(self):
        return self.__cantidad == 0

class Impresion:
    __tiempo_impresion: int
    __tiempo_espera: int

    def __init__(self, tiempo_impresion, tiempo_espera):
        self.__tiempo_impresion = tiempo_impresion
        self.__tiempo_espera = tiempo_espera
    
    def get_tiempo_impresion(self):
        return self.__tiempo_impresion

    def get_tiempo_espera(self):
        return self.__tiempo_espera


def llega_impresion(reloj):
    if reloj in (0,5,10,15,20,25):
        return True
    return False


if __name__ == "__main__":
    cola = ColaEncadenada()

    impresiones_pendientes = 0
    impresiones_realizadas = 0
    tiempo_espera_total = 0
    tiempo_ocupacion_impresora = 0
    reloj = 0
    tiempo_de_simulacion = 30
    
    while reloj < tiempo_de_simulacion:
        if llega_impresion(reloj):
            impresiones_pendientes += 1
            tiempo_impresion = int(input(f"Ingresa el tiempo de impresión (llegó en minuto {reloj}): "))
            cola.insertar(Impresion(tiempo_impresion, reloj))

        if not cola.vacia():
            if tiempo_ocupacion_impresora == 0:
                impresion_en_proceso = cola.suprimir()
                tiempo_restante = impresion_en_proceso.get_tiempo_impresion() - 5
                tiempo_espera_total += reloj - impresion_en_proceso.get_tiempo_espera()

                if tiempo_restante > 0:
                    tiempo_ocupacion_impresora = 5
                    cola.insertar(Impresion(tiempo_restante, reloj + 5))
                else:
                    tiempo_ocupacion_impresora = impresion_en_proceso.get_tiempo_impresion()
                    impresiones_realizadas += 1
                    impresiones_pendientes -= 1

        reloj += 1

        if tiempo_ocupacion_impresora > 0:
            tiempo_ocupacion_impresora -= 1