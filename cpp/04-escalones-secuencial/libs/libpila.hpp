#pragma once

#include "libsolucion.hpp"

class Pila {
private:
  int __capacidad;
  int __longitud;
  Solucion *__pila;

public:
  explicit Pila(int capacidad);
  ~Pila();
  void insertar(const Solucion &item);
  Solucion eliminar();
  bool vacia() const;
  bool llena() const;
};
