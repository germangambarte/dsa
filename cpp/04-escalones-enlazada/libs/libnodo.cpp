#include "libnodo.hpp"
#include "libsolucion.hpp"

Nodo::Nodo(const Solucion &item, Nodo *siguiente) {
  __item = item;
  __siguiente = siguiente;
};
const Solucion & Nodo::get_item() const{ return __item; }
void Nodo::set_item(const Solucion &item) { __item = item; }
Nodo *Nodo::get_siguiente() { return __siguiente; }
void Nodo::set_siguiente(Nodo *siguiente) { __siguiente = siguiente; }
