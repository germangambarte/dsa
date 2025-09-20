#pragma once

class ColaCircular {
private:
  int __capacidad;
  int __ultimo;
  int __primero;
  int __longitud;
  int *__cola;

public:
  explicit ColaCircular(int capacidad);
  ~ColaCircular();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
  bool llena() const;
};
