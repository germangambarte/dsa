#pragma once

#include <string>

class Solucion {
public:
  int n;
  std::string solucion;
  Solucion() : n(0), solucion("") {}
  Solucion(int n) : n(n), solucion("") {}
  Solucion(int n, std::string solucion) : n(n), solucion(solucion) {}
};
