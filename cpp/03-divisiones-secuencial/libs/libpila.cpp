#include "libpila.hpp"
#include <iostream>

using namespace std;

Pila::Pila(int capacidad) {
  __capacidad = capacidad;
  __longitud = 0;
  __pila = new int[capacidad];
}

Pila::~Pila() { delete[] __pila; }

void Pila::insertar(int item) {
  if (llena()) {
    cout << "pila llena." << endl;
    return;
  }
  __pila[__longitud++] = item;
}

int Pila::eliminar() {
  if (vacia()) {
    cout << "pila llena." << endl;
    return -1;
  }
  int temp = __pila[--__longitud];
  return temp;
}

void Pila::recorrer() const {
  int i = __longitud - 1;
  while (i >= 0) {
    cout << __pila[i] << " ";
    i--;
  }
  cout << endl;
}

bool Pila::vacia() const { return __longitud == 0; }

bool Pila::llena() const { return __longitud == __capacidad; }
