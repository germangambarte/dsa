#pragma once

class PilaSecuencial {
private:
  int __capacidad;
  int __longitud;
  int *__pila;

public:
  explicit PilaSecuencial(int capacidad);
  ~PilaSecuencial();
  void insertar(int item);
  int eliminar();
  void recorrer() const;
  bool vacia() const;
  bool llena() const;
};
