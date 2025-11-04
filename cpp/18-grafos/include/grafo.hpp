#pragma once
#include "lista.hpp"

class Grafo {
private:
    int _n;
    Lista* _lista;
    void _bep_visita();
    void _aciclica_visita();
    int* _min_dist();
    void dijkstra(int origen, int* d, int* c);

public:
    explicit Grafo(int n);
    ~Grafo();
    void agregar_arista(int a, int b, int peso);
    void camino(int a, int b);
    void aciclico();
    void adyacentes();
    void conexo();
    void bea();
    void bep();
};
