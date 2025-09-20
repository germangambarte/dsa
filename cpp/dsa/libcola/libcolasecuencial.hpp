#pragma once

class ColaSecuencial {
private:
  int __capacidad;
  int __ultimo;
  int __primero;
  int *__cola;

public:
  explicit ColaSecuencial(int capacidad);
  ~ColaSecuencial();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
  bool llena() const;
};
