#include "../PilaSecuencial.h"
#include <iostream>

void simularFactorial(int numero) {
  PilaSecuencial pila(numero + 1);
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
