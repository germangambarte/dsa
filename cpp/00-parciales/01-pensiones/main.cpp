#include <cstdlib>
#include <ctime>
#include <iostream>

class Nodo {
private:
  int _item;
  Nodo *_sig;

public:
  Nodo(int item, Nodo *sig = nullptr) : _item(item), _sig(sig) {}
  int get_item() { return _item; }
  Nodo *get_sig() { return _sig; }
  void set_sig(Nodo *sig) { _sig = sig; }
};

class Cola {
private:
  Nodo *_cab;
  Nodo *_cola;
  int _long;

public:
  Cola() {
    _cab = nullptr;
    _cola = nullptr;
    _long = 0;
  }
  ~Cola() {
    while (!vacia()) {
      eliminar();
    }
  }
  void insertar(int item) {
    Nodo *nuevo_nodo = new Nodo(item);
    if (vacia()) {
      _cab = nuevo_nodo;
    } else {
      _cola->set_sig(nuevo_nodo);
    }
    _cola = nuevo_nodo;
    _long++;
  }
  int eliminar() {
    auto temp = _cab;
    _cab = _cab->get_sig();
    _long--;
    int temp_item = temp->get_item();
    delete temp;
    return temp_item;
  }
  void recorrer() {
    auto actual = _cab;
    while (actual) {
      std::cout << actual->get_item() << " ";
      actual = actual->get_sig();
    }
    std::cout << std::endl;
  }
  bool vacia() { return _long == 0; }
};

int numero_random(int ref) {
  std::srand(std::time(nullptr));
  return std::rand() % ref;
}

int main() {
  const int N = 2;
  auto cajeros = new Cola *[2]{new Cola(), new Cola()};
  auto tiempo_atención = new int[2]{6, 4};
  auto atendidos = new int[2]{0, 0};
  int duracion = 60 * 5;
  int reloj = 0;

  while (reloj < duracion + 1) {
    if (reloj % 3 == 0 and numero_random(N) == 1) {
      cajeros[numero_random(N)]->insertar(1);
    }
    int i = 0;
    while (i < N) {
      if (reloj % tiempo_atención[i] == 0 and numero_random(N) == 1) {
        cajeros[i]->eliminar();
        atendidos[i]++;
      }
      i++;
    }
    reloj++;
  }

  std::cout << "El cajero 1 atendió: " << atendidos[0] << " pensionados"
            << std::endl;
  std::cout << "El cajero 2 atendió: " << atendidos[1] << " pensionados"
            << std::endl;
  return 0;
}
