#include "../../include/ColaCircular.hpp"

int main() {
  auto cola = new ColaCircular(3);
  cola->insertar(1);
  cola->insertar(2);
  cola->insertar(3);

  cola->recorrer();

  cola->insertar(4);

  cola->eliminar();

  cola->recorrer();

  cola->insertar(1);

  cola->recorrer();
  return 0;
}
