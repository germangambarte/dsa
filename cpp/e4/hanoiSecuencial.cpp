#include "../PilaSecuencial.h"
#include <cmath>
#include <iostream>

void mostrarDiscos(PilaSecuencial &pila1, PilaSecuencial &pila2,
                   PilaSecuencial &pila3) {
  std::cout << "Pila 1" << std::endl;
  pila1.recorrer();
  std::cout << "Pila 2" << std::endl;
  pila2.recorrer();
  std::cout << "Pila 3" << std::endl;
  pila3.recorrer();
}

bool intentarMovimiento(PilaSecuencial &pilaA, PilaSecuencial &pilaB) {
  if (pilaA.vacia()) {
    return 0;
  }

  int a = pilaA.suprimir();

  if (pilaB.vacia()) {
    pilaB.insertar(a);
    return 1;
  } else {
    int b = pilaB.suprimir();
    pilaB.insertar(b);
    if (a < b) {
      pilaB.insertar(a);
      return 1;
    } else {
      pilaA.insertar(a);
      return 0;
    }
  }
}

bool mover(PilaSecuencial &pila1, PilaSecuencial &pila2,
           PilaSecuencial &pila3) {
  int origen, destino;
  std::cout << "Ingrese pila de origen: ";
  std::cin >> origen;
  std::cout << "Ingrese pila de destino: ";
  std::cin >> destino;
  std::cout << std::endl;
  if (origen == 1) {
    if (destino == 2) {
      return intentarMovimiento(pila1, pila2);
    } else if (destino == 3) {
      return intentarMovimiento(pila1, pila3);
    } else {
      std::cout << "Pila de destino no valido";
    }
  } else if (origen == 2) {
    if (destino == 1) {
      return intentarMovimiento(pila2, pila1);
    } else if (destino == 3) {
      return intentarMovimiento(pila2, pila3);
    } else {
      std::cout << "Pila de destino no valido";
    }
  } else if (origen == 3) {
    if (destino == 1) {
      return intentarMovimiento(pila3, pila1);
    } else if (destino == 2) {
      return intentarMovimiento(pila3, pila2);
    } else {
      std::cout << "Pila de destino no valido";
    }
  } else {
    std::cout << "Pila de origen no valido.";
  }
  return 0;
}

int main() {
  int discos, movimientosMinimos;

  std::cout << "ingrese la cantidad de discos: ";
  std::cin >> discos;
  std::cout << std::endl;
  movimientosMinimos = pow(2, discos) - 1;

  PilaSecuencial pila1(discos), pila2(discos), pila3(discos);

  while (discos > 0) {
    pila1.insertar(discos--);
  }

  mostrarDiscos(pila1, pila2, pila3);

  int cantidadMovimientos = 0;

  while (!pila1.vacia() || !pila2.vacia()) {

    if (mover(pila1, pila2, pila3)) {
      std::cout << "Movimiento Realizado!" << std::endl;
      cantidadMovimientos++;
    } else {
      std::cout << "Movimiento no valido." << std::endl;
    }
    mostrarDiscos(pila1, pila2, pila3);
    std::cout << "-----------------------" << std::endl;
  }
  std::cout << "Movimientos realizados: " << cantidadMovimientos << std::endl;
  std::cout << "Movimientos minimos: " << movimientosMinimos << std::endl;

  return 0;
}
