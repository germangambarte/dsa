#pragma once

class Nodo {
private:
    int _nodo;
    int _peso;
    Nodo* _sig;

public:
    Nodo(int item);
    Nodo(int item, Nodo* sig);
    int get_nodo();
    void set_nodo(int nodo);
    int get_peso();
    void set_peso(int peso);
    Nodo& get_sig();
    void set_sig(Nodo* sig);
};
