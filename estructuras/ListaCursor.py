import numpy as np


class Nodo:
    __items: int
    __siguiente: int

    def cargar_item(self, items: int):
        self.__items = items

    def obtener_item(self):
        return self.__items

    def cargar_siguiente(self, siguiente: int):
        self.__siguiente = siguiente

    def obtener_siguiente(self):
        return self.__siguiente


class ListaCursor:
    __dimension: int
    __cantidad: int
    __cabeza: int
    __disponible: int
    __lista: np.ndarray

    def __init__(self, dim: int):
        self.__dimension = dim
        self.__cantidad = 0
        self.__cabeza = 0
        self.__disponible = 0
        self.__lista = np.empty(dim, dtype=Nodo)
        for i in range(dim):
            self.__lista[i] = Nodo()

    def obtener_disponible(self):
        i = 0
        while i < self.__dimension and self.__lista[i].obtener_siguiente() != None:
            i += 1

        if i < self.__dimension:
            self.__disponible = i
            return True

        self.__disponible = None
        return False

    def liberar_disponible(self, posicion: int):
        if 0 > posicion >= self.__dimension:
            print("Posicion no valida.")
            return False
        self.__lista[posicion].cargar_siguiente(None)
        return True

    def insertar_posicion(self, posicion: int, item: int):
        if self.__cantidad == self.__dimension or not self.obtener_disponible():
            print("Lista llena.")
            return None
        if 0 > posicion >= self.__dimension:
            print("Posicion no valida.")
            return None
        self.__lista[self.__disponible].cargar_item(item)
        anterior_cabeza = cabeza = self.__cabeza
        i = 0
        while i < posicion:
            anterior_cabeza = cabeza
            cabeza = self.__lista[cabeza].obtener_siguiente()
            i += 1

        if cabeza == self.__cabeza:  # Insertar al principio
            if self.vacia():
                self.__lista[self.__disponible].cargar_siguiente(-1)
            else:
                self.__lista[self.__disponible].cargar_siguiente(self.__cabeza)
            self.__cabeza = self.__disponible
        elif cabeza == -1:  # insertar al final
            self.__lista[self.__disponible].cargar_siguiente(-1)
            self.__lista[anterior_cabeza].cargar_siguiente(self.__disponible)
        else:
            self.__lista[self.__disponible].cargar_siguiente(cabeza)
            self.__lista[anterior_cabeza].cargar_siguiente(self.__disponible)
        self.__cantidad += 1
        return item

    def insertar_contenido(self, item: int):
        if self.__cantidad == self.__dimension or not self.obtener_disponible():
            print("Lista llena.")
            return None
        self.__lista[self.__disponible].cargar_item(item)
        anterior_cabeza = cabeza = self.__cabeza
        while cabeza != -1 and self.__lista[cabeza].obtener_item() < item:
            anterior_cabeza = cabeza
            cabeza = self.__lista[cabeza].obtener_siguiente()

        if cabeza == self.__cabeza:  # insertar al principio(nueva cabeza)
            if self.vacia():
                self.__lista[self.__disponible].cargar_siguiente(-1)
            else:
                self.__lista[self.__disponible].cargar_siguiente(cabeza)
            self.__cabeza = self.__disponible
        elif cabeza == -1:  # insertar al final(ultimo elemento)
            self.__lista[self.__disponible].cargar_siguiente(-1)
            self.__lista[anterior_cabeza].cargar_siguiente(self.__disponible)
        else:  # inserta entre cabeza y anterior_cabeza
            self.__lista[self.__disponible].cargar_siguiente(cabeza)
            self.__lista[anterior_cabeza].cargar_siguiente(self.__disponible)
            pass
        self.__cantidad += 1
        return item

    def suprimir(self, posicion: int):
        if self.vacia():
            print("Lista vacia.")
            return None
        if 0 > posicion >= self.__dimension:
            print("Posicion no valida.")
            return None
        anterior_cabeza = cabeza = self.__disponible
        i = 0
        while i < posicion:
            anterior_cabeza = cabeza
            cabeza = self.__lista[cabeza].obtener_siguiente()
            i += 1
        if cabeza == self.__cabeza:
            if self.vacia():
                self.__cabeza = 0
            else:
                self.__cabeza = self.__lista[anterior_cabeza].obtener_siguiente()
        else:
            auxiliar = self.__lista[cabeza].obtener_siguiente()
            self.__lista[anterior_cabeza].cargar_siguiente(auxiliar)
        eliminado = self.__lista[cabeza].obtener_item()
        self.liberar_disponible(cabeza)
        self.__cantidad -= 1
        return eliminado

    def recuperar(self, posicion: int):
        if self.vacia():
            print("Lista vacia.")
            return None
        if 0 > posicion >= self.__dimension:
            print("Posicion no valida.")
            return None
        cabeza = self.__cabeza
        i = 0
        while i < posicion:
            cabeza = self.__lista[cabeza].obtener_siguiente()
            i += 1
        return self.__lista[cabeza].obtener_item()

    def buscar(self, item: int):
        if self.vacia():
            print("Lista vacia.")
            return None
        cabeza = self.__cabeza
        i = 0
        while i < self.__dimension and self.__lista[cabeza].obtener_item() != item:
            cabeza = self.__lista[cabeza].obtener_siguiente()

        if i == self.__dimension:
            print("Elemento no encontrado.")
            return None
        return i + 1

    def vacia(self):
        return self.__cantidad == 0

    def recorrer(self):
        cabeza = self.__cabeza
        i = 0
        while i < self.__dimension:
            print(self.__lista[cabeza].obtener_item(), end=" ")
            cabeza = self.__lista[cabeza].obtener_siguiente()
            i += 1
        print("\n")


if __name__ == "__main__":
    lista = ListaCursor(4)

    lista.insertar_contenido(1)
    lista.insertar_contenido(2)
    lista.insertar_contenido(3)
    lista.insertar_contenido(4)
    lista.insertar_contenido(5)

    lista.recorrer()

    lista.suprimir(4)
    lista.suprimir(3)

    lista.recorrer()
