#pragma once

#include "libsolucion.hpp"

class Nodo {
private:
  Solucion __item;
  Nodo *__siguiente;

public:
  explicit Nodo(const Solucion &item, Nodo *siguiente = nullptr);
  const Solucion &get_item() const;
  void set_item(const Solucion &item);
  Nodo *get_siguiente();
  void set_siguiente(Nodo *siguiente);
};
