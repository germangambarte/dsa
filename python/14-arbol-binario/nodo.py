class Nodo:
    __clave: int
    __izq: "Nodo | None"
    __der: "Nodo | None"

    def __init__(self, clave: int, izq=None, der=None) -> None:
        self.__clave = clave
        self.__izq = izq
        self.__der = der

    def get_clave(self):
        return self.__clave

    def get_izq(self):
        return self.__izq

    def get_der(self):
        return self.__der

    def set_clave(self, clave):
        self.__clave = clave

    def set_izq(self, izq):
        self.__izq = izq

    def set_der(self, der):
        self.__der = der
