#include <cmath>
#include <libpila.hpp>

class Hanoi {
private:
  Pila *__torres;
  int __movimientos;
  int __movimientos_minimos;
  int __discos;

public:
  Hanoi(int discos) : __discos(discos) {
    __movimientos = 0;
    __movimientos_minimos = std::pow(__discos, 2) - 1;
    Pila *pila_cargada = new Pila(__discos);
    for (int i = __discos; i > 0; i--) {
      pila_cargada->insertar(i);
    }
    __torres = Pila[3]{pila_cargada, new Pila(__discos), new Pila(__discos)};
  }
};

int main() {
  auto hanoi = new Hanoi(3);
  return 0;
}
