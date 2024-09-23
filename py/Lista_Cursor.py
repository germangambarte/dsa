import numpy as np


class Nodo:
    def __init__(self):
        self.__item = None
        self.__siguiente_posicion = None

    def set_item(self, x):
        self.__item = x

    def get_item(self):
        return self.__item

    def set_siguiente_posicion(self, siguiente_posicion):
        self.__siguiente_posicion = siguiente_posicion

    def get_siguiente_posicion(self):
        return self.__siguiente_posicion


class Lista:
    __maximo: int
    __cabeza: int
    __cantidad: int
    __disponible: int
    __espacio: np.ndarray

    def __init__(self, maximo):
        self.__maximo = maximo
        self.__cabeza = 0
        self.__cantidad = 0
        self.__disponible = 0
        self.__espacio = np.empty(maximo, dtype=Nodo)
        for i in range(self.__maximo):
            self.__espacio[i] = Nodo()

    def vacia(self):
        return self.__cantidad == 0

    def get_disponible(self):
        i = 0
        while i < self.__maximo and self.__espacio[i].get_siguiente_posicion() != None:
            i += 1
        if i < self.__maximo:
            self.__disponible = i
            return True
        else:
            self.__disponible = None
            return False

    def liberar_disponible(self, posicion: int):
        if 0 <= posicion < self.__maximo:
            self.__espacio[posicion].set_siguiente_posicion(None)
            return True
        return False

    def insertar_por_posicion(self, item, posicion):
        if (
            self.__cantidad < self.__maximo
            and 0 <= posicion <= self.__cantidad
            and self.get_disponible()
        ):
            self.__espacio[self.__disponible].set_item(item)
            ant = cabeza = self.__cabeza
            i = 0
            while i < posicion:
                ant = cabeza
                cabeza = self.__espacio[cabeza].get_siguiente_posicion()
                i += 1
            if cabeza == self.__cabeza:  # Inserta al inicio
                if self.vacia():
                    self.__espacio[self.__cabeza].set_siguiente_posicion(-1)
                else:
                    self.__espacio[self.__disponible].set_siguiente_posicion(
                        self.__cabeza
                    )
                self.__cabeza = self.__disponible
            elif cabeza == -1:  # Inserta al final
                self.__espacio[self.__disponible].set_siguiente_posicion(-1)
                self.__espacio[ant].set_siguiente_posicion(self.__disponible)
            else:
                self.__espacio[self.__disponible].set_siguiente_posicion(cabeza)
                self.__espacio[ant].set_siguiente_posicion(self.__disponible)
            self.__cantidad += 1
            return True
        print("Espacio lleno o posición incorrecta.")
        return False

    def insertar_por_contenido(self, item):
        if self.__cantidad < self.__maximo and self.get_disponible():
            anterior = cabeza = self.__cabeza
            self.__espacio[self.__disponible].set_item(item)
            while cabeza != -1 and self.__espacio[cabeza].get_item() < item:
                anterior = cabeza
                cabeza = self.__espacio[cabeza].get_siguiente_posicion()
            if cabeza == self.__cabeza:  # Inserta al inicio
                if self.__cantidad == 0:
                    self.__espacio[self.__cabeza].set_siguiente_posicion(-1)
                else:
                    self.__espacio[self.__disponible].set_siguiente_posicion(
                        self.__cabeza
                    )
                self.__cabeza = self.__disponible
            elif cabeza == -1:  # Inserta al final
                self.__espacio[self.__disponible].set_siguiente_posicion(-1)
                self.__espacio[anterior].set_siguiente_posicion(self.__disponible)
            else:
                self.__espacio[self.__disponible].set_siguiente_posicion(cabeza)
                self.__espacio[anterior].set_siguiente_posicion(self.__disponible)
            self.__cantidad += 1
            return True
        print("Espacio lleno.")
        return False

    def suprimir(self, posicion):
        if self.vacia():
            print("Lista vacia.")
            return -1
        if self.__cantidad != 0 and 0 <= posicion < self.__cantidad:
            anterior = cabeza = self.__cabeza
            i = 0
            while i < posicion:
                anterior = cabeza
                cabeza = self.__espacio[cabeza].get_siguiente_posicion()
                i += 1
            if cabeza == self.__cabeza:  # Elimina el primer elemento
                self.__cabeza = (
                    self.__espacio[anterior].get_siguiente_posicion()
                    if self.__cantidad > 1
                    else 0
                )
            else:
                self.__espacio[anterior].set_siguiente_posicion(
                    self.__espacio[cabeza].get_siguiente_posicion()
                )
            eliminado = self.__espacio[cabeza].get_item()
            self.liberar_disponible(cabeza)
            self.__cantidad -= 1
            return eliminado
        else:
            print("Posicion no valida.")
            return -1

    def recuperar(self, posicion):
        if self.vacia():
            print("Lista vacia.")
            return -1
        if self.__cantidad != 0 and 0 <= posicion < self.__cantidad:
            cabeza = self.__cabeza
            i = 0
            while i < posicion:
                cabeza = self.__espacio[cabeza].get_siguiente_posicion()
                i += 1
            return self.__espacio[cabeza].get_item()
        print("Lista vacía o posición incorrecta.")
        return 0

    def buscar(self, item):
        if self.vacia():
            print("Lista vacia.")
            return -1
        i = 0
        cabeza = self.__cabeza
        while i < self.__cantidad and self.__espacio[cabeza].get_item() != item:
            cabeza = self.__espacio[cabeza].get_siguiente_posicion()
            i += 1
        if i < self.__cantidad:
            return i + 1
        else:
            print("Elemento no encontrado.")
            return -1

    def recorrer(self):
        if self.vacia():
            print("Lista vacia.")
            return
        if self.__cantidad != 0:
            cabeza = self.__cabeza
            print("Lista:", end=" ")
            while cabeza != -1:
                print(self.__espacio[cabeza].get_item(), end=" ")
                cabeza = self.__espacio[cabeza].get_siguiente_posicion()
            print()


if __name__ == "__main__":
    lista = Lista(5)
    # ---- insertar_por_posicion ----
    # lista.insertar_por_posicion(1, 0)
    # lista.insertar_por_posicion(2, 1)
    # lista.insertar_por_posicion(3, 0)
    # lista.insertar_por_posicion(4, 2)
    # lista.insertar_por_posicion(5, 1)
    # lista.recorrer()
    # ---- insertar_por_contenido ----
    lista.insertar_por_contenido(3)
    lista.insertar_por_contenido(5)
    lista.insertar_por_contenido(1)
    lista.insertar_por_contenido(4)
    lista.insertar_por_contenido(2)
    lista.recorrer()
    # ---- suprimir_por_contenido ----
    lista.suprimir(2)
    lista.recorrer()
    # ---- suprimir_por_posicion ----
    lista.insertar_por_posicion(7, 2)
    lista.recorrer()
    print(f"buscar: {lista.buscar(7)}")
    print(f"recuperar: {lista.recuperar(lista.buscar(7)-1)}")
