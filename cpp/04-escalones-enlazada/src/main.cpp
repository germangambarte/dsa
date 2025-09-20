#include "libsolucion.hpp"
#include <iostream>
#include <libpila.hpp>
#include <string>

void hallar_caminos_recursivo(int n, std::string solucion) {
  if (n == 0) {
    std::cout << solucion << std::endl;
    return;
  }
  if (n >= 1) {
    hallar_caminos_recursivo(n - 1, solucion + "1");
  }
  if (n >= 2) {
    hallar_caminos_recursivo(n - 2, solucion + "2");
  }
}

void hallar_caminos(Pila *p) {
  while (!p->vacia()) {
    auto camino = p->eliminar();
    if (camino.n == 0) {
      std::cout << camino.solucion << std::endl;
    }
    if (camino.n >= 1) {
      p->insertar(Solucion(camino.n - 1, camino.solucion + "1"));
    }
    if (camino.n >= 2) {
      p->insertar(Solucion(camino.n - 2, camino.solucion + "2"));
    }
  }
}

int main() {
  auto pila = new Pila();
  pila->insertar(Solucion(5));
  hallar_caminos(pila);
  std::cout << std::endl;
  // hallar_caminos_recursivo(5, "");
  return 0;
}
