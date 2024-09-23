#include "../PilaEncadenada.h"
#include <iostream>

void simularFactorial(int numero) {
  PilaEncadenada pila;
  while (numero > 0) {
    pila.insertar(numero);
    numero--;
  }
  int resultado = 1;
  while (!pila.vacia()) {
    resultado *= pila.suprimir();
  }

  std::cout << "resultado: " << resultado << std::endl;
}

int main() {
  simularFactorial(6);
  return 0;
}
