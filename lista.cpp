#include <iostream>

class Nodo {
public:
  int item;
  Nodo *siguiente;

  Nodo(int valor) : item(valor), siguiente(nullptr){};
};

class Cola {
private:
  Nodo *cabeza;
  int cantidad;

public:
  Cola() : cabeza(nullptr), cantidad(0) {}

  ~Cola() {
    while (!vacia()) {
      suprimir();
    }
  }

  void insertar(int item) {
    Nodo *nuevoNodo = new Nodo(item);
    nuevoNodo->siguiente = cabeza;
    cabeza = nuevoNodo;
    cantidad++;
  }

  void suprimir() {
    if (vacia()) {
      std::cout << "Pila vacia." << std::endl;
    } else {
      Nodo *nodoAEliminar = cabeza;
      cabeza = cabeza->siguiente;
      delete nodoAEliminar;
      cantidad--;
    }
  }

  void recorrer() {
    Nodo *actual = cabeza;
    while (actual != nullptr) {
      std::cout << actual->item << " ";
      actual = actual->siguiente;
    }
    std::cout << std::endl;
  }

  bool vacia() { return cantidad == 0; }
};

void conversionBinaria(int decimal) {
  Cola pila;

  int valorActual = decimal;
  while (valorActual >= 2) {
    pila.insertar(valorActual % 2);
    valorActual /= 2;
  }
  pila.insertar(valorActual % 2);

  while (!pila.vacia()) {
  }
  pila.recorrer();
}

int main() {
  conversionBinaria(23519);
  return 0;
}
