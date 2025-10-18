class NodoArbol:
    """Representa un nodo en el Árbol Binario Balanceado."""

    def __init__(self, clave, dato=1):
        self.clave = clave  # Valor de la clave (key)
        self.contador = dato  # Contador de ocurrencias (con)
        self.factor_balanceo = 0  # Factor de balanceo (bal)

        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBalanceado:
    """Implementa las operaciones de un Árbol Binario de Búsqueda Balanceado (AVL)."""

    def __init__(self):
        self.raiz = None

    # --- Métodos Auxiliares de Rotación (Mantienen la lógica original de Wirth) ---

    def _rotacion_simple_izquierda(self, nodo_p):
        nodo_p1 = nodo_p.hijo_derecho
        nodo_p.hijo_derecho = nodo_p1.hijo_izquierdo
        nodo_p1.hijo_izquierdo = nodo_p
        return nodo_p1

    def _rotacion_simple_derecha(self, nodo_p):
        nodo_p1 = nodo_p.hijo_izquierdo
        nodo_p.hijo_izquierdo = nodo_p1.hijo_derecho
        nodo_p1.hijo_derecho = nodo_p
        return nodo_p1

    def _rotacion_doble_izquierda(self, nodo_p):
        nodo_p1 = nodo_p.hijo_izquierdo
        nodo_p2 = nodo_p1.hijo_derecho

        nodo_p1.hijo_derecho = nodo_p2.hijo_izquierdo
        nodo_p2.hijo_izquierdo = nodo_p1

        nodo_p.hijo_izquierdo = nodo_p2.hijo_derecho
        nodo_p2.hijo_derecho = nodo_p

        if nodo_p2.factor_balanceo == -1:
            nodo_p.factor_balanceo = 1
            nodo_p1.factor_balanceo = 0
        elif nodo_p2.factor_balanceo == 1:
            nodo_p.factor_balanceo = 0
            nodo_p1.factor_balanceo = -1
        else:  # nodo_p2.factor_balanceo == 0
            nodo_p.factor_balanceo = 0
            nodo_p1.factor_balanceo = 0

        nodo_p2.factor_balanceo = 0
        return nodo_p2

    def _rotacion_doble_derecha(self, nodo_p):
        nodo_p1 = nodo_p.hijo_derecho
        nodo_p2 = nodo_p1.hijo_izquierdo

        nodo_p1.hijo_izquierdo = nodo_p2.hijo_derecho
        nodo_p2.hijo_derecho = nodo_p1

        nodo_p.hijo_derecho = nodo_p2.hijo_izquierdo
        nodo_p2.hijo_izquierdo = nodo_p

        if nodo_p2.factor_balanceo == 1:
            nodo_p.factor_balanceo = -1
            nodo_p1.factor_balanceo = 0
        elif nodo_p2.factor_balanceo == -1:
            nodo_p.factor_balanceo = 0
            nodo_p1.factor_balanceo = 1
        else:  # nodo_p2.factor_balanceo == 0
            nodo_p.factor_balanceo = 0
            nodo_p1.factor_balanceo = 0

        nodo_p2.factor_balanceo = 0
        return nodo_p2

    # --- Rebalanceo después de Supresión (balani y baland en C++) ---

    def _rebalancear_tras_supresion_derecha(self, nodo_p):
        """Implementa la lógica de balani (supresión en la izquierda -> balancear derecha)."""
        altura_disminuyo = False

        if nodo_p.factor_balanceo == -1:
            nodo_p.factor_balanceo = 0
        elif nodo_p.factor_balanceo == 0:
            nodo_p.factor_balanceo = 1
            altura_disminuyo = True
        elif nodo_p.factor_balanceo == 1:
            # Rebalancear
            nodo_p1 = nodo_p.hijo_derecho
            b1 = nodo_p1.factor_balanceo

            if b1 >= 0:  # Rotación simple izquierda
                nodo_p = self._rotacion_simple_izquierda(nodo_p)
                if b1 == 0:
                    nodo_p.factor_balanceo = -1
                    nodo_p.hijo_izquierdo.factor_balanceo = 1
                    altura_disminuyo = False
                else:
                    nodo_p.factor_balanceo = 0
                    nodo_p.hijo_izquierdo.factor_balanceo = 0
                    altura_disminuyo = True
            else:  # Rotación doble derecha-izquierda
                nodo_p = self._rotacion_doble_derecha(nodo_p)
                nodo_p.factor_balanceo = 0
                altura_disminuyo = True

        return nodo_p, altura_disminuyo

    def _rebalancear_tras_supresion_izquierda(self, nodo_p):
        """Implementa la lógica de baland (supresión en la derecha -> balancear izquierda)."""
        altura_disminuyo = False

        if nodo_p.factor_balanceo == 1:
            nodo_p.factor_balanceo = 0
        elif nodo_p.factor_balanceo == 0:
            nodo_p.factor_balanceo = -1
            altura_disminuyo = False
        elif nodo_p.factor_balanceo == -1:
            # Rebalancear
            nodo_p1 = nodo_p.hijo_izquierdo
            b1 = nodo_p1.factor_balanceo

            if b1 <= 0:  # Rotación simple derecha
                nodo_p = self._rotacion_simple_derecha(nodo_p)
                if b1 == 0:
                    nodo_p.factor_balanceo = 1
                    nodo_p.hijo_derecho.factor_balanceo = -1
                    altura_disminuyo = False
                else:
                    nodo_p.factor_balanceo = 0
                    nodo_p.hijo_derecho.factor_balanceo = 0
                    altura_disminuyo = True
            else:  # Rotación doble izquierda-derecha
                nodo_p = self._rotacion_doble_izquierda(nodo_p)
                nodo_p.factor_balanceo = 0
                altura_disminuyo = True

        return nodo_p, altura_disminuyo

    # --- Funciones de Supresión ---

    def suprimir(self, clave):
        """Función principal para suprimir una clave del árbol."""
        # 'altura_disminuyo' (h en C++) es True si la altura de la rama disminuyó tras la supresión
        nueva_raiz, altura_disminuyo = self._suprimir_recursivo(self.raiz, clave)
        self.raiz = nueva_raiz

    def _sucesor_inorden(self, nodo_r):
        """Encuentra el nodo para sustituir (el nodo más a la derecha del subárbol izquierdo, como en el código C++)."""
        if nodo_r.hijo_derecho is None:
            # Encontramos el sucesor (el nodo más a la derecha)
            # Retorna el nodo, y True para 'altura_disminuyo' ya que este nodo será eliminado.
            return nodo_r, nodo_r.hijo_izquierdo, True

        # Continúa buscando a la derecha
        nodo_r.hijo_derecho, nuevo_sucesor, altura_disminuyo = self._sucesor_inorden(
            nodo_r.hijo_derecho
        )

        if altura_disminuyo:
            # Rebalancear después de la eliminación en la derecha
            nodo_r, altura_disminuyo = self._rebalancear_tras_supresion_izquierda(
                nodo_r
            )

        return nodo_r, nuevo_sucesor, altura_disminuyo

    def _suprimir_recursivo(self, nodo_p, clave):
        """Implementación recursiva de la supresión con rebalanceo."""
        if nodo_p is None:
            print("La llave no está en el árbol.")
            return None, False

        altura_disminuyo = False

        if clave < nodo_p.clave:
            # Buscar en la izquierda
            nodo_p.hijo_izquierdo, altura_disminuyo = self._suprimir_recursivo(
                nodo_p.hijo_izquierdo, clave
            )
            if altura_disminuyo:
                # Rebalancear el nodo_p, ya que la rama izquierda disminuyó
                nodo_p, altura_disminuyo = self._rebalancear_tras_supresion_derecha(
                    nodo_p
                )

        elif clave > nodo_p.clave:
            # Buscar en la derecha
            nodo_p.hijo_derecho, altura_disminuyo = self._suprimir_recursivo(
                nodo_p.hijo_derecho, clave
            )
            if altura_disminuyo:
                # Rebalancear el nodo_p, ya que la rama derecha disminuyó
                nodo_p, altura_disminuyo = self._rebalancear_tras_supresion_izquierda(
                    nodo_p
                )

        else:
            # ¡Nodo encontrado! (p->key == x)
            if nodo_p.contador > 1:
                nodo_p.contador -= 1
                altura_disminuyo = False  # La altura no cambia
            else:
                # Eliminar nodo_p
                if nodo_p.hijo_izquierdo is None and nodo_p.hijo_derecho is None:
                    # Caso 1: Hoja
                    nodo_p = None
                    altura_disminuyo = True
                elif nodo_p.hijo_izquierdo is None:
                    # Caso 2a: Solo hijo derecho
                    nodo_p = nodo_p.hijo_derecho
                    altura_disminuyo = True
                elif nodo_p.hijo_derecho is None:
                    # Caso 2b: Solo hijo izquierdo
                    nodo_p = nodo_p.hijo_izquierdo
                    altura_disminuyo = True
                else:
                    # Caso 3: Dos hijos (reemplazar con el predecesor inorden, el nodo más a la derecha del subárbol izquierdo)

                    # El código C++ usa el nodo más a la DERECHA del subárbol IZQUIERDO para reemplazar.
                    # Esto corresponde al predecesor inorden, aunque la función C++ se llama 'sup' (supresor)
                    # y recorre a la derecha del subárbol izquierdo.

                    # Llamar a _sucesor_inorden, que devuelve el nodo reemplazante (sucesor),
                    # el subárbol izquierdo actualizado y si la altura disminuyó.
                    nodo_p.hijo_izquierdo, nodo_reemplazante, altura_disminuyo = (
                        self._sucesor_inorden(nodo_p.hijo_izquierdo)
                    )

                    # Copiar clave y contador del reemplazante al nodo actual
                    nodo_p.clave = nodo_reemplazante.clave
                    nodo_p.contador = nodo_reemplazante.contador

                    # El reemplazante ha sido eliminado de su posición original, ahora debemos rebalancear
                    if altura_disminuyo:
                        nodo_p, altura_disminuyo = (
                            self._rebalancear_tras_supresion_derecha(nodo_p)
                        )

        return nodo_p, altura_disminuyo

    # --- (El resto de los métodos: insertar, mostrar, ejecutar_menu, etc.) ---

    # --- Inserción ---

    def insertar(self, clave):
        """Función principal para insertar una clave en el árbol."""
        nueva_raiz, altura_crecio = self._insertar_recursivo(self.raiz, clave)
        self.raiz = nueva_raiz

    def _insertar_recursivo(self, nodo_p, clave):
        """Implementación recursiva de la inserción con rebalanceo (omito el código completo aquí por espacio, pero iría aquí)."""
        # ... (código de inserción del ejemplo anterior) ...
        # Copiamos la lógica de inserción completa para que la clase sea funcional:
        if nodo_p is None:
            return NodoArbol(clave), True

        altura_crecio = False

        if clave < nodo_p.clave:
            nodo_p.hijo_izquierdo, altura_crecio = self._insertar_recursivo(
                nodo_p.hijo_izquierdo, clave
            )
            if altura_crecio:
                if nodo_p.factor_balanceo == 1:
                    nodo_p.factor_balanceo = 0
                    altura_crecio = False
                elif nodo_p.factor_balanceo == 0:
                    nodo_p.factor_balanceo = -1
                    altura_crecio = True
                elif nodo_p.factor_balanceo == -1:
                    nodo_p1 = nodo_p.hijo_izquierdo
                    if nodo_p1.factor_balanceo == -1:
                        nodo_p = self._rotacion_simple_derecha(nodo_p)
                        nodo_p.factor_balanceo = 0
                        nodo_p.hijo_derecho.factor_balanceo = 0
                    else:
                        nodo_p = self._rotacion_doble_izquierda(nodo_p)
                    altura_crecio = False
        elif clave > nodo_p.clave:
            nodo_p.hijo_derecho, altura_crecio = self._insertar_recursivo(
                nodo_p.hijo_derecho, clave
            )
            if altura_crecio:
                if nodo_p.factor_balanceo == -1:
                    nodo_p.factor_balanceo = 0
                    altura_crecio = False
                elif nodo_p.factor_balanceo == 0:
                    nodo_p.factor_balanceo = 1
                    altura_crecio = True
                elif nodo_p.factor_balanceo == 1:
                    nodo_p1 = nodo_p.hijo_derecho
                    if nodo_p1.factor_balanceo == 1:
                        nodo_p = self._rotacion_simple_izquierda(nodo_p)
                        nodo_p.factor_balanceo = 0
                        nodo_p.hijo_izquierdo.factor_balanceo = 0
                    else:
                        nodo_p = self._rotacion_doble_derecha(nodo_p)
                    altura_crecio = False
        else:
            nodo_p.contador += 1
            altura_crecio = False

        return nodo_p, altura_crecio

    # --- Mostrar ---

    def mostrar_arbol_inorden(self):
        """Muestra el árbol en recorrido Inorden."""
        print("Recorrido Inorden (Clave, Factor Balanceo, Contador):")
        self._mostrar_inorden_recursivo(self.raiz)
        print()  # Nueva línea al final

    def _mostrar_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_inorden_recursivo(nodo.hijo_izquierdo)
            print(
                f"({nodo.clave}, Bal: {nodo.factor_balanceo}, Cnt: {nodo.contador}) ",
                end="",
            )
            self._mostrar_inorden_recursivo(nodo.hijo_derecho)

    # --- Interfaz de usuario/Ejecución ---

    def ejecutar_menu(self):
        """Implementa el menú de la función main del código C++."""
        while True:
            print("\n--- Menú Árbol Balanceado (AVL) ---")
            print("1. Insertar")
            print("2. Suprimir")
            print("3. Mostrar (Inorden)")
            print("4. Salir")

            opcion = input("\nIngrese opción: ")

            if opcion == "1":
                self._manejar_insercion()
            elif opcion == "2":
                self._manejar_supresion()
            elif opcion == "3":
                self.mostrar_arbol_inorden()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def _manejar_insercion(self):
        """Maneja el bucle de inserción del menú."""
        print("Ingrese elemento a insertar (0 para finalizar):")
        while True:
            try:
                elemento = input("> ")
                if elemento == "0":
                    break
                clave = int(elemento)
                self.insertar(clave)
            except ValueError:
                print("Entrada no válida. Ingrese un número o 0.")

    def _manejar_supresion(self):
        """Maneja el bucle de supresión del menú."""
        print("Ingrese elemento a suprimir (0 para finalizar):")
        while True:
            try:
                elemento = input("> ")
                if elemento == "0":
                    break
                clave = int(elemento)
                self.suprimir(clave)
            except ValueError:
                print("Entrada no válida. Ingrese un número o 0.")


# --- Ejecución del Programa ---
if __name__ == "__main__":
    arbol = ArbolBalanceado()
    arbol.ejecutar_menu()
