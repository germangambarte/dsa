#pragma once
#include "libnodo.hpp"

class Pila {
private:
  int __longitud;
  Nodo *__cabeza;

public:
  ~Pila();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
};
