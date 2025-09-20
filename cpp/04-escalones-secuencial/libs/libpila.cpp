#include "libpila.hpp"
#include "libsolucion.hpp"
#include <iostream>

using namespace std;

Pila::Pila(int capacidad) {
  __capacidad = capacidad;
  __longitud = 0;
  __pila = new Solucion[capacidad];
}

Pila::~Pila() { delete[] __pila; }

void Pila::insertar(const Solucion &item) {
  if (llena()) {
    cout << "pila llena." << endl;
    return;
  }
  __pila[__longitud++] = item;
}

Solucion Pila::eliminar() {
  if (vacia()) {
    cout << "pila llena." << endl;
    return Solucion();
  }
  return __pila[--__longitud];
}

bool Pila::vacia() const { return __longitud == 0; }

bool Pila::llena() const { return __longitud == __capacidad; }
