#include "../../include/ColaEnlazada.hpp"

int main() {
  auto cola = new ColaEnlazada();
  cola->insertar(1);
  cola->insertar(2);
  cola->insertar(3);

  cola->recorrer();

  cola->eliminar();

  cola->recorrer();
  return 0;
}
