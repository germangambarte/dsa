import random

class Nodo:
    __item:int
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

class Cajero(ColaEncadenada):
  contador_clientes:int
  contador_atendidos:int
  total_tiempo_espera:int
  tiempo_maximo_espera:int
  total_tiempo_espera_incompleta:int
  tiempo_cajero:int
  tiempo_ocupado:int
  def __init__(self,tiempo_ocupado):
    super().__init__()
    self.contador_clientes = 0
    self.contador_atendidos = 0
    self.total_tiempo_espera = 0
    self.tiempo_maximo_espera = 0
    self.total_tiempo_espera_incompleta = 0
    self.tiempo_cajero = 0
    self.tiempo_ocupado = tiempo_ocupado

  def insertar_cliente(self, reloj):
    self.insertar(reloj)
    self.contador_clientes += 1
  
  def atender_cliente(self, reloj,tiempo_simulacion):
    if self.tiempo_cajero == 0 and not self.vacia():
      cliente_atendido = self.suprimir()
      tiempo_espera = reloj - cliente_atendido

      if reloj + self.tiempo_ocupado < tiempo_simulacion:
        # Si se puede terminar de atender
        self.total_tiempo_espera += tiempo_espera
        self.contador_atendidos +=1
      else:
        # Si el tiempo de atención no se puede completar
        self.total_tiempo_espera_incompleta += tiempo_espera
      
      if tiempo_espera > self.tiempo_maximo_espera:
        self.tiempo_maximo_espera = tiempo_espera

      self.tiempo_cajero = self.tiempo_ocupado

    elif self.tiempo_cajero>0:
      self.tiempo_cajero -= 1

  def obtener_datos(self):
      return {
          'tiempo_maximo_espera': self.tiempo_maximo_espera,
          'clientes_atendidos': self.contador_clientes,
          'clientes_sin_atender': self.contador_clientes - self.contador_atendidos,
          'promedio_espera_atendidos': (self.total_tiempo_espera / self.contador_atendidos) if self.contador_atendidos > 0 else 0,
          'promedio_espera_no_atendidos': (self.total_tiempo_espera_incompleta / (self.contador_clientes - self.contador_atendidos)) if (self.contador_clientes - self.contador_atendidos) > 0 else 0
      }
      

def llega_cliente(probabilidad_llegada=0.3):
    """
    Simula si un cliente llega o no en el instante actual.
    :param probabilidad_llegada: Probabilidad de que llegue un cliente (entre 0 y 1).
    :return: True si llega un cliente, False en caso contrario.
    """
    return random.random() < probabilidad_llegada

def elegir_cajero(*clientes_en_cola):
    """
    Elige el cajero con menos clientes en cola.
    :param clientes_en_cola: Cantidad de clientes pendientes en cada cajero.
    :return: El índice del cajero con menos clientes en cola (1, 2, o 3).
    """
    # Encontrar el índice del cajero con menos clientes en cola
    return clientes_en_cola.index(min(clientes_en_cola)) + 1


if __name__ == "__main__":
    # Crear los cajeros con sus respectivos tiempos de atención
    cajero1 = Cajero(5)
    cajero2 = Cajero(3)
    cajero3 = Cajero(4)

    tms = 120
    reloj = 0

    while reloj < tms:
        # Verificar si llega un cliente
        if llega_cliente():
            cajero_elegido = elegir_cajero(
                cajero1.contador_clientes - cajero1.contador_atendidos,
                cajero2.contador_clientes - cajero2.contador_atendidos,
                cajero3.contador_clientes - cajero3.contador_atendidos
            )
            if cajero_elegido == 1:
                cajero1.insertar_cliente(reloj)
            elif cajero_elegido == 2:
                cajero2.insertar_cliente(reloj)
            else:
                cajero3.insertar_cliente(reloj)
        
        # Atender clientes si es posible
        cajero1.atender_cliente(reloj, tms)
        cajero2.atender_cliente(reloj, tms)
        cajero3.atender_cliente(reloj, tms)

        reloj += 1

    # Mostrar resultados
    datos_cajero1 = cajero1.obtener_datos()
    datos_cajero2 = cajero2.obtener_datos()
    datos_cajero3 = cajero3.obtener_datos()

    print(f"El tiempo máximo de espera en el cajero 1 es: {datos_cajero1['tiempo_maximo_espera']}")
    print(f"El tiempo máximo de espera en el cajero 2 es: {datos_cajero2['tiempo_maximo_espera']}")
    print(f"El tiempo máximo de espera en el cajero 3 es: {datos_cajero3['tiempo_maximo_espera']}")

    print(f"El total de clientes atendidos es: {datos_cajero1['clientes_atendidos'] + datos_cajero2['clientes_atendidos'] + datos_cajero3['clientes_atendidos']}")
    print(f"El total de clientes sin atender es: {datos_cajero1['clientes_sin_atender'] + datos_cajero2['clientes_sin_atender'] + datos_cajero3['clientes_sin_atender']}")

    print(f"Promedio de espera de los clientes atendidos:")
    print(f"Cajero 1: {datos_cajero1['promedio_espera_atendidos']}")
    print(f"Cajero 2: {datos_cajero2['promedio_espera_atendidos']}")
    print(f"Cajero 3: {datos_cajero3['promedio_espera_atendidos']}")

    print(f"Promedio de espera de los clientes sin atender:")
    print(f"Cajero 1: {datos_cajero1['promedio_espera_no_atendidos']}")
    print(f"Cajero 2: {datos_cajero2['promedio_espera_no_atendidos']}")
    print(f"Cajero 3: {datos_cajero3['promedio_espera_no_atendidos']}")
