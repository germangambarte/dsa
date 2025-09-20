#include "libpila.hpp"
#include "libsolucion.hpp"
#include <iostream>
using namespace std;

Pila::Pila() : __longitud(0), __cabeza(nullptr) {}

Pila::~Pila() {
  while (__cabeza) {
    eliminar();
  }
}

void Pila::insertar(const Solucion &item) {
  Nodo *nodo = new Nodo(item, __cabeza);
  __cabeza = nodo;
  __longitud++;
}

Solucion Pila::eliminar() {
  if (vacia()) {
    cout << "pila vacia." << endl;
    return -1;
  }
  Nodo *temp = __cabeza;
  auto temp_item = temp->get_item();
  __cabeza = __cabeza->get_siguiente();
  delete temp;
  return temp_item;
}

bool Pila::vacia() const { return __longitud == 0; }
