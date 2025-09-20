#pragma once

class Pila {
private:
  int __capacidad;
  int __longitud;
  int *__pila;

public:
  explicit Pila(int capacidad);
  ~Pila();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
  bool llena() const;
};
