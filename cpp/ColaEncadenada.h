#include "Nodo.h"
#include <iostream>
#ifndef COLAENCADENADA_H
#define COLAENCADENADA_H

class ColaEncadenada {
  int cantidad;
  Nodo *primero;
  Nodo *ultimo;

public:
  ColaEncadenada(int cant = 0)
      : cantidad(cant), primero(nullptr), ultimo(nullptr) {}

  int insertar(int item) {
    Nodo *nuevo = new Nodo();
    nuevo->cargarItem(item);
    nuevo->cargarSiguiente(nullptr);
    if (ultimo == nullptr) {
      primero = nuevo;
    } else {
      ultimo->cargarSiguiente(nuevo);
    }
    ultimo = nuevo;
    cantidad++;
    return ultimo->obtenerItem();
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Cola vacia." << std::endl;
      return 0;
    } else {
      Nodo *aux = primero;
      int itemEliminado = aux->obtenerItem();
      primero = primero->obtenerSiguiente();
      cantidad--;
      delete aux;
      return itemEliminado;
    }
  }

  void recorrer() {
    Nodo *actual = primero;
    while (actual != nullptr) {
      std::cout << actual->obtenerItem() << " ";
      actual = actual->obtenerSiguiente();
    }
    std::cout << std::endl;
  }

  Nodo *recuperarPrimero() { return primero; }

  int vacia() { return cantidad == 0; }
};

// int main() {
//   ColaEncadenada cola(3);
//   cola.insertar(1);
//   cola.insertar(2);
//   cola.insertar(3);
//   cola.insertar(4);
//   cola.insertar(5);
//
//   cola.recorrer();
//
//   cola.suprimir();
//   cola.suprimir();
//
//   cola.recorrer();
//   return 0;
// }
#endif
