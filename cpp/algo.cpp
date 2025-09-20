#include <iostream>
#include <string>

class Solucion {
public:
  int n;
  std::string solucion;

  Solucion(int n) : n(n), solucion("") {}
  Solucion(int n, std::string solucion) : n(n), solucion(solucion) {}
};

class Nodo {
private:
  Solucion __item;
  Nodo *__siguiente;

public:
  Nodo(const Solucion &item) : __item(item), __siguiente(nullptr) {}
  Nodo(const Solucion &item, Nodo *siguiente)
      : __item(item), __siguiente(siguiente) {}
  Solucion &get_item() { return __item; }
  void set_item(const Solucion &item) { __item = item; }
  Nodo *get_siguiente() { return __siguiente; }
  void set_siguiente(Nodo *siguiente) { __siguiente = siguiente; }
};

class Pila {
private:
  int __longitud;
  Nodo *__cabeza;

public:
  Pila() : __longitud(0), __cabeza(nullptr) {}
  ~Pila() {
    while (!vacia()) {
      eliminar();
    }
  }
  void insertar(const Solucion &item) {
    auto nuevo = new Nodo(item, __cabeza);
    __cabeza = nuevo;
    __longitud++;
  }
  Solucion eliminar() {
    if (vacia()) {
      std::cout << "pila vacia." << std::endl;
    }

    Nodo *temp = __cabeza;
    Solucion temp_sol = __cabeza->get_item();
    __cabeza = temp->get_siguiente();
    delete temp;
    __longitud--;
    return temp_sol;
  }
  bool vacia() { return __longitud == 0; }
};

void hallar_camino(Pila *p) {
  while (!p->vacia()) {
    Solucion camino = p->eliminar();
    if (camino.n == 0) {
      std::cout << camino.solucion << std::endl;
    }
    if (camino.n >= 1) {
      p->insertar(Solucion(camino.n - 1, camino.solucion + "1"));
    }
    if (camino.n >= 2) {
      p->insertar(Solucion(camino.n - 2, camino.solucion + "2"));
    }
  }
}

int main() {
  auto pila = new Pila();
  pila->insertar(Solucion(5));
  hallar_camino(pila);
  return 0;
}
