import numpy as np

ORDEN = 2


"""Representa una entrada de clave en un nodo (struct item en C++)."""
class Clave:
    valor: int# valor de la clave
    repeticiones: int # contador de duplicados
    derecha: "Pagina | None" # puntero al hijo derecho de esta clave

    def __init__(self, valor: int, repeticiones=1) -> None:
        self.valor = valor
        self.repeticiones = repeticiones
        self.derecha = None

    def __lt__(self, otro):
        if isinstance(otro, "Clave"):
            return self.valor < otro.valor
        return self.valor < otro

    def __eq__(self, otro):
        if isinstance(otro, "Clave"):
            return self.valor == otro.valor
        return self.valor == otro

    def __repr__(self):
        return f"({self.valor}: {self.repeticiones})"


"""Representa una página del árbol B (struct page en C++)."""
class Pagina:
    capacidad: int 
    longitud: int
    izquierda: "Clave | None" # Puntero al hijo mas a la izquierda
    claves: np.ndarray # lista de objetos Clave

    def __init__(self,capacidad) -> None:
        self.capacidad = 2 * capacidad -1
        self.longitud = 0
        self.izquierda = None
        self.claves = np.empty(2 * ORDEN)

    def lleno(self):
        return self.longitud == self.capacidad

class ArbolBalanceado:
    __raiz: Pagina | None
