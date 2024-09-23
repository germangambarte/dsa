#include <iostream>
#ifndef PILASECUENCIAL_H
#define PILASECUENCIAL_H

class PilaSecuencial {
private:
  int *items, cantidad, tope, dimension;

public:
  PilaSecuencial(int dim = 0) : dimension(dim) {
    tope = -1;
    cantidad = 0;
    items = new int[dimension];
  }

  int insertar(int item) {
    if (cantidad < dimension) {
      items[++tope] = item;
      cantidad++;
      return item;
    } else {
      std::cout << "Pila llena." << std::endl;
      return 0;
    }
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Pila vacia." << std::endl;
      return 0;
    } else {
      cantidad--;
      return items[tope--];
    }
  }

  void recorrer() {
    for (int i = tope; i >= 0; i--) {
      std::cout << items[i] << " ";
    }
    std::cout << std::endl;
  }

  bool vacia() { return tope == -1; }
};

#endif // PILASECUENCIAL_H
