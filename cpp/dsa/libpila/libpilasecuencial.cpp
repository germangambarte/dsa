#include "libpilasecuencial.hpp"
#include <iostream>

using namespace std;

PilaSecuencial::PilaSecuencial(int capacidad) {
  __capacidad = capacidad;
  __longitud = 0;
  __pila = new int[capacidad];
}

PilaSecuencial::~PilaSecuencial() { delete[] __pila; }

void PilaSecuencial::insertar(int item) {
  if (llena()) {
    cout << "pila llena." << endl;
    return;
  }
  __pila[__longitud++] = item;
}

int PilaSecuencial::eliminar() {
  if (vacia()) {
    cout << "pila llena." << endl;
    return -1;
  }
  int temp = __pila[--__longitud];
  return temp;
}

void PilaSecuencial::recorrer() const {
  int i = __longitud - 1;
  while (i >= 0) {
    cout << __pila[i] << " ";
    i--;
  }
  cout << endl;
}

bool PilaSecuencial::vacia() const { return __longitud == 0; }

bool PilaSecuencial::llena() const { return __longitud == __capacidad; }
