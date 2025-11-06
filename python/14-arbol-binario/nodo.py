class Nodo:
    __clave: int
    __izq: "Nodo"
    __der: "Nodo"

    def __init__(self, clave: int, izq=None, der=None):
        self.__clave = clave
        self.__izq = izq
        self.__der = der

    def get_clave(self):
        return self.__clave

    def set_clave(self, clave: int):
        self.__clave = clave

    def get_izq(self):
        return self.__izq

    def set_izq(self, izq):
        self.__izq = izq

    def get_der(self):
        return self.__der

    def set_der(self, der):
        self.__der = der
