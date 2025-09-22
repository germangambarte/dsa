from listas.enlazada_contenido import Lista, Termino


class Polinomio(Lista):
    def __init__(self) -> None:
        super().__init__()

    def __operacion(self, polinomio: "Polinomio", signo: int):
        resultado = Polinomio()
        max_exponente = max(self.get_max_exponente(), polinomio.get_max_exponente())
        exponente = 0
        while exponente <= max_exponente:
            termino1 = self.recuperar(Termino(exponente=exponente))
            termino2 = polinomio.recuperar(Termino(exponente=exponente))
            coeficiente = 0
            if termino1 is not None:
                coeficiente += termino1.get_coeficiente()
            if termino2 is not None:
                coeficiente += signo * termino2.get_coeficiente()
            resultado.insertar(Termino(coeficiente, exponente))
            exponente += 1
        return resultado

    def suma(self, polinomio: "Polinomio"):
        return self.__operacion(polinomio, 1)

    def resta(self, polinomio: "Polinomio"):
        return self.__operacion(polinomio, -1)

    def multiplicacion(self, polinomio: "Polinomio"):
        resultado = Polinomio()
        exponente = 0
        while exponente <= self.get_max_exponente():
            termino1 = self.recuperar(Termino(exponente=exponente))
            j = 0
            while j <= polinomio.get_max_exponente() and termino1 is not None:
                termino2 = polinomio.recuperar(Termino(exponente=j))
                if termino2 is not None:
                    resultado.insertar(
                        Termino(
                            termino1.get_coeficiente() * termino2.get_coeficiente(),
                            termino1.get_exponente() + termino2.get_exponente(),
                        )
                    )
                j += 1
            exponente += 1
        return resultado


if __name__ == "__main__":
    polinomio1 = Polinomio()
    polinomio2 = Polinomio()
    polinomio1.insertar(Termino(3, 2))
    polinomio1.insertar(Termino(5, 3))
    polinomio1.insertar(Termino(2, 0))
    polinomio1.insertar(Termino(1, 2))

    polinomio2.insertar(Termino(2, 1))
    polinomio2.insertar(Termino(1, 2))
    polinomio2.insertar(Termino(1, 2))

    print("polinomio1:", end=" ")
    polinomio1.recorrer()
    print("polinomio2:", end=" ")
    polinomio2.recorrer()
    resultado = polinomio1.suma(polinomio2)
    print("suma:", end=" ")
    resultado.recorrer()
    resultado = polinomio1.resta(polinomio2)
    print("resta:", end=" ")
    resultado.recorrer()
    resultado = polinomio1.multiplicacion(polinomio2)
    print("multiplicación:", end=" ")
    resultado.recorrer()
