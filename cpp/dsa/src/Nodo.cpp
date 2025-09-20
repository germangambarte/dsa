#include "../include/Nodo.hpp"

Nodo::Nodo(int item, Nodo *siguiente) {
  __item = item;
  __siguiente = siguiente;
};
int Nodo::get_item() { return __item; }
void Nodo::set_item(int item) { __item = item; }
Nodo *Nodo::get_siguiente() { return __siguiente; }
void Nodo::set_siguiente(Nodo *siguiente) { __siguiente = siguiente; }
