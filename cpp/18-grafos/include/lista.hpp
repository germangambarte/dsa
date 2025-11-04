#pragma once
#include "nodo.hpp"

class Lista{
private:
  int _long;
  Nodo * _cab;
public:
  explicit Lista();
  ~Lista();
  void insertar(int nodo,int peso);
  int buscar(int nodo);
  int recuperar(int i);
  void recorrer();
  int suprimir(int nodo);
};
