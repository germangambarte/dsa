#include "../include/cola.hpp"
#include <iostream>

Cola::Cola(int cap)
{
    _cap = cap;
    _long = 0;
    _pri = 0;
    _ult = 0;
    _cola = new int[cap];
}

Cola::~Cola()
{
    while (_long > 0) {
        Cola::suprimir();
    }
}

void Cola::insertar(int item)
{
    if (_long == _cap) {
        std::cout << "cola llena" << std::endl;
        return;
    }
    _cola[_ult] = item;
    _ult = (_ult + 1) % _cap;
    _long++;
}

int Cola::suprimir()
{
    if (_long == 0) {
        std::cout << "cola vacia." << std::endl;
        return -1;
    }
    auto temp = _cola[_pri];
    _pri = (_pri + 1) % _cap;
    _long--;
    return temp;
}
