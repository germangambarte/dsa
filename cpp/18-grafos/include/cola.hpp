#pragma once

class Cola {
private:
    int _ult;
    int _pri;
    int* _cola;
    int _cap;
    int _long;

public:
    explicit Cola(int cap);
    ~Cola();
    void insertar(int item);
    int suprimir();
};
