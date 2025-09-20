#include "../../include/ColaSecuencial.hpp"

int main() {
  auto cola = new ColaSecuencial(3);
  cola->insertar(1);
  cola->insertar(2);
  cola->insertar(3);

  cola->recorrer();

  cola->insertar(4);

  cola->eliminar();

  cola->recorrer();
  return 0;
}
