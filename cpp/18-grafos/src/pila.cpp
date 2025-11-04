#include "../include/pila.hpp"
#include <iostream>

Pila::Pila(int cap)
{
    _cap = cap;
    _long = 0;
    _ult = -1;
    _pila = new int[_cap];
}

Pila::~Pila()
{
    while (_long > 0) {
        suprimir();
    }
}

void Pila::insertar(int item)
{
    if (_long == _cap) {
        std::cout << "pila llena." << std::endl;
        return;
    }
    _pila[++_ult] = item;
    _long++;
}

int Pila::suprimir(){
  if (_long == 0){
	std::cout << "pila vacia." << std::endl;
	return -1;
  }
  auto temp = _pila[_ult--];
  _long--;
  return temp;
}
