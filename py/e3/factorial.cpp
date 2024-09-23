#include <iostream>
#include <vector>

class Pila {
private:
  std::vector<int> items;
  int cantidad;
  int tope;
  int dimension;

public:
  Pila(int dim) : cantidad(0), tope(0), dimension(dim) {
    items.resize(dimension);
  }

  int get_tope() { return tope; }

  void insertar(int item) {
    if (cantidad == dimension) {
      dimension += 5;
      items.resize(dimension);
    }

    items[tope] = item;
    tope++;
    cantidad++;
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Pila vacia." << std::endl;
    } else {
      tope--;
      cantidad--;
    }
    return items[tope];
  }

  void recorrer() {
    for (int i = tope - 1; i >= 0; i--) {
      std::cout << items[i] << " ";
    }
    std::cout << std::endl;
  }

  bool vacia() { return cantidad == 0; }
};

int factorial(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

void simularFactorial(int valor) {
  Pila pila(3);
  while (valor > 0) {
    int resultadoFactorial = factorial(valor - 1);
    pila.insertar(valor * resultadoFactorial);
    valor -= 1;
  }
  pila.insertar(1);
  int resultado;
  while (!pila.vacia()) {
    resultado = pila.suprimir();
  }
  std::cout << "factorial: " << resultado << std::endl;
}

int main() {
  simularFactorial(5);
  return 0;
}
