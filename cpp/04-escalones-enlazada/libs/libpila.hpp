#pragma once
#include "libnodo.hpp"
#include "libsolucion.hpp"

class Pila {
private:
  int __longitud;
  Nodo *__cabeza;

public:
  explicit Pila();
  ~Pila();
  void insertar(const Solucion &item);
  Solucion eliminar();
  bool vacia() const;
};
