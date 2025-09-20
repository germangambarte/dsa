#pragma once

#include "Nodo.hpp"

class ColaEnlazada {
private:
  int __longitud;
  Nodo *__cabeza;
  Nodo *__cola;

public:
  ~ColaEnlazada();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
};
