#include "Nodo.h"
#include <iostream>

#ifndef PILAENCADENADA_H
#define PILAENCADENADA_H

class PilaEncadenada {
  Nodo *tope;
  int cantidad;

public:
  PilaEncadenada(Nodo *top = nullptr, int cant = 0)
      : tope(top), cantidad(cant) {}

  int insertar(int item) {
    Nodo *nodo;
    nodo = new Nodo();
    nodo->cargarItem(item);
    nodo->cargarSiguiente(tope);
    tope = nodo;
    cantidad++;
    return nodo->obtenerItem();
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Pila vacia." << std::endl;
      return 0;
    } else {
      Nodo *aux = tope;
      int item = aux->obtenerItem();
      tope = tope->obtenerSiguiente();
      cantidad--;
      delete aux;
      return (item);
    }
  }

  void recorrer() {
    Nodo *actual = tope;
    while (actual != nullptr) {
      std::cout << actual->obtenerItem() << " ";
      actual = actual->obtenerSiguiente();
    }
    std::cout << std::endl;
  }

  int muestraTope() { return tope->obtenerItem(); }

  Nodo *recuperaTope() { return tope; }

  int vacia() { return cantidad == 0; }
};

#endif // PILAENCADENADA_H
