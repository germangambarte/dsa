#include "../include/lista.hpp"
#include "../include/nodo.hpp"
#include <iostream>

Lista::Lista()
{
    _cab = nullptr;
    _long = 0;
}

Lista::~Lista()
{
    auto actual = _cab;
    Nodo* anterior = nullptr;
    while (_long > 0) {
        anterior = actual;
        actual = actual->get_sig();
        delete anterior;
    }
    _long = 0;
}

void Lista::insertar(int nodo, int peso = 1)
{
    auto nuevo = new Nodo(nodo, peso);
    auto actual = _cab;
    Nodo* anterior = nullptr;
    while (actual and actual->get_nodo() < nodo) {
        anterior = actual;
        actual = actual->get_sig();
    }
    nuevo->set_sig(anterior->get_sig());
    anterior->set_sig(nuevo);
    _long++;
}

int Lista::suprimir(int nodo)
{
    if (_long == 0) {
        std::cout << "lista vacia." << std::endl;
        return -1;
    }
    auto actual = _cab;
    Nodo* anterior = nullptr;
    while (actual and actual->get_nodo() != nodo) {
        anterior = actual;
        actual = actual->get_sig();
    }
    auto temp = actual;
    anterior->set_sig(actual->get_sig());
    return temp->get_peso();
}

int Lista::buscar(int nodo)
{
    int i = 0;
    auto actual = _cab;
    while (actual and actual->get_nodo() != nodo) {
        actual = actual->get_sig();
    }
    return actual ? i : -1;
}

int Lista::recuperar(int nodo)
{
    int posicion = buscar(nodo);
    if (posicion == -1) {
        std::cout << "No se encontró el nodo" << std::endl;
        return -1;
    }
    auto actual = _cab;
    int i = 0;
    while (i <= posicion) {
        actual = actual->get_sig();
        i++;
    }
    return actual->get_peso();
}

void Lista::recorrer()
{
    auto actual = _cab;
    while (actual) {
        std::cout << actual->get_nodo() << " ";
    }
    std::cout << std::endl;
}
