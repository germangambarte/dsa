#include <iostream>
#ifndef NODO_H
#define NODO_H

class Nodo {
  int item;
  Nodo *siguiente;

public:
  int obtenerItem() { return item; }

  Nodo *obtenerSiguiente() { return siguiente; }

  void cargarItem(int nuevoItem) { item = nuevoItem; }

  void cargarSiguiente(Nodo *nuevoSiguiente) { siguiente = nuevoSiguiente; }
};

#endif
