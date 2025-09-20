#include "../../include/PilaEnlazada.hpp"

int main() {
  auto pila = new PilaEnlazada();
  pila->insertar(1);
  pila->insertar(2);
  pila->insertar(3);
  pila->insertar(4);

  pila->recorrer();

  pila->eliminar();

  pila->recorrer();

  return 0;
}
