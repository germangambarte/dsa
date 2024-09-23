class Nodo:
  __item: int
  __siguiente: "Nodo"

  def __init__(self,item=0,siguiente=None):
    self.__item = item
    self.__siguiente = siguiente
  
  def get_item(self):
    return self.__item
  
  def get_siguiente(self):
    return self.__siguiente
  
  def set_item(self, item):
    self.__item = item

  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente

class PilaEncadenada:
  __dimension:int
  __cantidad:int
  __tope:Nodo

  def __init__(self, dimension):
    self.__dimension = dimension 
    self.__cantidad = 0
    self.__tope = None

  def insertar(self, item):
    if self.__cantidad == self.__dimension:
      print("Pila llena.")
      return None
    nuevo_nodo = Nodo(item)
    nuevo_nodo.set_siguiente(self.__tope)
    self.__tope = nuevo_nodo
    self.__cantidad+=1
    return item
  
  def suprimir(self):
    if self.vacia():
      print("Pila vacia.")
      return None
    eliminado = self.__tope
    self.__tope = self.__tope.get_siguiente()
    self.__cantidad -=1
    return eliminado
  
  def recorrer(self):
    if self.vacia():
      print("Pila vacia.")
      return None
    actual = self.__tope
    while actual is not None:
      print(actual.get_item(), end=" ")
      actual = actual.get_siguiente()
    print("\n")
  
  def vacia(self):
    return self.__cantidad == 0

if __name__ == "__main__":
  pila = PilaEncadenada(4)

  pila.insertar(1)
  pila.insertar(2)
  pila.insertar(3)
  pila.insertar(4)
  pila.insertar(5)

  pila.recorrer()

  pila.suprimir()
  pila.suprimir()

  pila.recorrer()