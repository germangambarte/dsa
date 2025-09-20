#include "../include/ColaEnlazada.hpp"
#include <iostream>
using namespace std;

ColaEnlazada::~ColaEnlazada() {
  while (!vacia()) {
    eliminar();
  }
}

void ColaEnlazada::insertar(int item) {
  Nodo *nodo = new Nodo(item);
  if (vacia()) {
    __cabeza = nodo;
  } else {
    __cola->set_siguiente(nodo);
  }
  __cola = nodo;
  __longitud++;
}

int ColaEnlazada::eliminar() {
  if (vacia()) {
    cout << "cola vacia." << endl;
    return -1;
  }
  Nodo *temp = __cabeza;
  int temp_item = temp->get_item();

  __cabeza = __cabeza->get_siguiente();
  __longitud--;
  delete temp;
  return temp_item;
}

void ColaEnlazada::recorrer() const {
  Nodo *actual = __cabeza;
  while (actual) {
    cout << actual->get_item() << " ";
    actual = actual->get_siguiente();
  }
  cout << endl;
  delete actual;
}

bool ColaEnlazada::vacia() const { return __longitud == 0; }
