#include "../include/ColaCircular.hpp"
#include <iostream>

using namespace std;

ColaCircular::ColaCircular(int capacidad) : __capacidad(capacidad) {
  __primero = 0;
  __ultimo = 0;
  __longitud = 0;
  __cola = new int[capacidad];
}

ColaCircular::~ColaCircular() { delete[] __cola; }

void ColaCircular::insertar(int item) {
  if (llena()) {
    cout << "cola llena." << endl;
    return;
  }
  __cola[__ultimo] = item;
  __ultimo = (__ultimo + 1) % __capacidad;
  __longitud++;
}

int ColaCircular::eliminar() {
  if (vacia()) {
    cout << "cola vacia." << endl;
    return -1;
  }
  auto temp = __cola[__primero];

  __primero = (__primero + 1) % __capacidad;
  __longitud--;

  return temp;
}

void ColaCircular::recorrer() const {
  int i = __primero;
  int j = 0;
  while (j < __longitud) {
    cout << __cola[i] << " ";
    i = (i + 1) % __capacidad;
    j++;
  }
  cout << endl;
}

bool ColaCircular::vacia() const { return __longitud == 0; }

bool ColaCircular::llena() const { return __longitud == __capacidad; }
