#include <iostream>
#ifndef PILASECUENCIAL_H
#define PILASECUENCIAL_H

class ColaSecuencial {
  int *items, primero, ultimo, cantidad, maximo;

public:
  ColaSecuencial(int max = 0) : maximo(max) {
    items = new int[max];
    primero = 0;
    ultimo = 0;
    cantidad = 0;
  }

  int insertar(int item) {
    if (cantidad < maximo) {
      items[ultimo] = item;
      ultimo = (ultimo + 1) % maximo;
      cantidad++;
      return item;
    } else {
      return 0;
    }
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Pila vacia" << std::endl;
      return 0;
    } else {
      int eliminado = items[primero];
      primero = (primero + 1) % maximo;
      cantidad--;
      return eliminado;
    }
  }

  int vacia() { return cantidad == 0; }

  void recorrer() {
    if (!vacia()) {
      for (int i = primero, j = 0; j < cantidad; i = (i + 1) % maximo, j++) {
        std::cout << items[i] << std::endl;
      }
    }
  }
};

#endif
