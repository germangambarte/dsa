#pragma once

class Pila {
private:
  int _ult;
  int* _pila;
  int _cap;
  int _long;
public:
  explicit Pila(int cap);
  ~Pila();
  void insertar(int item);
  int suprimir();
};
