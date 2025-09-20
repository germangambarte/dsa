#include "libpila.hpp"
#include <iostream>
using namespace std;


Pila::~Pila() {
  while (__cabeza) {
    eliminar();
  }
}

void Pila::insertar(int item) {
  Nodo *nodo = new Nodo(item, __cabeza);
  __cabeza = nodo;
  __longitud++;
}

int Pila::eliminar() {
  if (vacia()) {
    cout << "pila vacia." << endl;
    return -1;
  }
  Nodo *temp = __cabeza;
  __cabeza = __cabeza->get_siguiente();
  return temp->get_item();
}

void Pila::recorrer() const {
  Nodo *actual = __cabeza;
  while (actual) {
    cout << actual->get_item() << " ";
    actual = actual->get_siguiente();
  }
  cout << endl;
}

bool Pila::vacia() const { return __longitud == 0; }
