#include <libpilasecuencial.hpp>

int main() {
  PilaSecuencial *pila = new PilaSecuencial(3);
  pila->insertar(1);
  pila->insertar(2);
  pila->insertar(3);
  pila->insertar(4);

  pila->recorrer();

  pila->eliminar();

  pila->recorrer();

  return 0;
}
