#pragma once

class Nodo {
private:
  int __item;
  Nodo *__siguiente;

public:
  explicit Nodo(int item, Nodo *siguiente = nullptr);
  int get_item();
  void set_item(int item);
  Nodo *get_siguiente();
  void set_siguiente(Nodo *siguiente);
};
