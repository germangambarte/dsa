#include "../include/PilaEnlazada.hpp"
#include "../include/Nodo.hpp"
#include <iostream>
using namespace std;

PilaEnlazada::PilaEnlazada() {
  __longitud = 0;
  __cabeza = nullptr;
}

PilaEnlazada::~PilaEnlazada() {
  while (__cabeza) {
    eliminar();
  }
}

void PilaEnlazada::insertar(int item) {
  Nodo *nodo = new Nodo(item, __cabeza);
  __cabeza = nodo;
  __longitud++;
}

int PilaEnlazada::eliminar() {
  if (vacia()) {
    cout << "pila vacia." << endl;
    return -1;
  }
  Nodo *temp = __cabeza;
  __cabeza = __cabeza->get_siguiente();
  return temp->get_item();
}

void PilaEnlazada::recorrer() const {
  Nodo *actual = __cabeza;
  while (actual) {
    cout << actual->get_item() << " ";
    actual = actual->get_siguiente();
  }
  cout << endl;
}

bool PilaEnlazada::vacia() const { return __longitud == 0; }
