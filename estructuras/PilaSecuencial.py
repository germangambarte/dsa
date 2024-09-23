import numpy as np

class PilaSecuencial:
  __dimension: int
  __cantidad: int
  __tope: int
  __items: np.ndarray

  def __init__(self, dimension):
    self.__dimension = dimension
    self.__cantidad = 0  
    self.__tope = -1
    self.__items = np.empty(dimension,dtype=int)
  
  def insertar(self, item):
    if self.__cantidad < self.__dimension:
      self.__tope +=1
      self.__items[self.__tope] = item
      self.__cantidad +=1
      return item
    else:
      print("Pila llena.")
      return None

  def suprimir(self):
    if self.vacia():
      print("Pila vacia.")
      return None
    eliminado = self.__items[self.__tope] 
    self.__tope -=1
    self.__cantidad -=1
    return eliminado

  def recorrer(self):
    for i in range(self.__tope, -1, -1):
      print(self.__items[i], end=" ")
    print("\n")

  def vacia(self):
    return self.__cantidad == 0    

if __name__ == "__main__":
  pila = PilaSecuencial(4)

  pila.insertar(1)
  pila.insertar(2)
  pila.insertar(3)
  pila.insertar(4)
  pila.insertar(5)

  pila.recorrer()

  pila.suprimir()
  pila.suprimir()

  pila.recorrer()