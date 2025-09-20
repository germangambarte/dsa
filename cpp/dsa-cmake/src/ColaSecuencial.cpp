#include "../include/ColaSecuencial.hpp"
#include <iostream>

using namespace std;

ColaSecuencial::ColaSecuencial(int capacidad) : __capacidad(capacidad) {
  __primero = 0;
  __ultimo = 0;
  __cola = new int[capacidad];
}

void ColaSecuencial::insertar(int item) {
  if (llena()) {
    cout << "cola llena." << endl;
    return;
  }
  __cola[__ultimo++] = item;
}

int ColaSecuencial::eliminar() {
  if (vacia()) {
    cout << "cola vacia." << endl;
    return -1;
  }
  int temp = __cola[__primero];
  int i = __primero;
  while (i < __ultimo - 1) {
    __cola[i] = __cola[i + 1];
    i++;
  }
  __ultimo--;
  return temp;
}

void ColaSecuencial::recorrer() const {
  int i = __primero;
  while (i < __ultimo) {
    cout << __cola[i] << " ";
    i++;
  }
  cout << endl;
}

bool ColaSecuencial::vacia() const { return __ultimo == __primero; }

bool ColaSecuencial::llena() const { return __ultimo == __capacidad; }
