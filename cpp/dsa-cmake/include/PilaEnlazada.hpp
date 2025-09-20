#pragma once
#include "Nodo.hpp"

class PilaEnlazada {
private:
  int __longitud;
  Nodo *__cabeza;

public:
  explicit PilaEnlazada();
  ~PilaEnlazada();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
};
