#include <libpila.hpp>

void divisiones_sucesivas(Pila *p, int n) {
  if (n < 2) {
    p->insertar(n);
    return;
  }
  p->insertar((int)n % 2);
  divisiones_sucesivas(p, (int)n / 2);
}

int main() {
  auto pila = new Pila(10);
  divisiones_sucesivas(pila, 100);
  pila->recorrer();
  return 0;
}
