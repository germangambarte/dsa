#include "../PilaSecuencial.h"
#include <iostream>

void convertirABinario(int numero) {
  PilaSecuencial pila(16);

  while (numero > 1) {
    pila.insertar(numero % 2);
    numero = numero / 2;
  }
  pila.insertar(numero % 2);

  while (!pila.vacia()) {
    std::cout << pila.suprimir();
  }
  std::cout << std::endl;
}

int main() {
  convertirABinario(1235);
  return 0;
}
