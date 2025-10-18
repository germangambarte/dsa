#include <algorithm>
#include <iostream>
using namespace std;

class Nodo {
private:
    int _clave;
    Nodo* _izq;
    Nodo* _der;

public:
    Nodo(int item, Nodo* izq = nullptr, Nodo* der = nullptr)
    {
        _clave = item;
        _izq = izq;
        _der = der;
    }

    int get_clave() { return _clave; }

    void set_clave(int item) { _clave = item; }

    Nodo*& get_izq() { return _izq; }

    void set_izq(Nodo* izq) { _izq = izq; }

    Nodo*& get_der() { return _der; }

    void set_der(Nodo* der) { _der = der; }

    // Comparación con un nodo
    bool operator<(Nodo& otro) const { return _clave < otro.get_clave(); }

    bool operator>(Nodo& otro) const { return _clave > otro.get_clave(); }

    bool operator==(Nodo& otro) const { return _clave == otro.get_clave(); }

    // Comparación con un entero
    bool operator<(int otro) const { return _clave < otro; }

    bool operator>(int otro) const { return _clave > otro; }

    bool operator==(int otro) const { return _clave == otro; }
};

class Arbol {
private:
    Nodo* _raiz;

    int _grado(Nodo* nodo)
    {
        int resultado = 0;
        if (nodo->get_izq())
            resultado++;
        if (nodo->get_der())
            resultado++;
        return resultado;
    }

    bool _es_igual(Nodo* nodo, int item)
    {
        return nodo and *nodo == item;
    }

    Nodo* _maximo(Nodo* actual)
    {
        if (not actual->get_der())
            return actual;
        return _maximo(actual->get_der());
    }

    Nodo* _suprimir(Nodo*& actual, int item)
    {
        if (not actual) {
            cout << "no existe el nodo " << item << endl;
            return nullptr;
        }
        if (actual->get_clave() == item) {
            switch (_grado(actual)) {
            case 0:
                delete actual;
                return nullptr;
            case 1:
                if (actual->get_izq()) {
                    auto temp = actual->get_izq();
                    delete actual;
                    return temp;
                }
                if (actual->get_der()) {
                    auto temp = actual->get_der();
                    delete actual;
                    return temp;
                }
            case 2:
                Nodo* max = _maximo(actual->get_izq());
                actual->set_clave(max->get_clave());
                actual->set_izq(_suprimir(actual->get_izq(), actual->get_clave()));
            }
        } else if (actual->get_clave() > item) {
            actual->set_izq(_suprimir(actual->get_izq(), item));
        } else {
            actual->set_der(_suprimir(actual->get_der(), item));
        }
        return actual;
    }

    void _insertar(Nodo*& actual, int item)
    {
        if (not actual) {
            actual = new Nodo(item);
            return;
        }
        _insertar(_obtener_sig(actual, item), item);
    }

    bool _padre(Nodo*& actual, int hijo, int padre)
    {
        if (_grado(actual) == 0) {
            cout << "el hijo no existe" << endl;
            return false;
        }
        if (actual->get_clave() == padre) {
            switch (_grado(actual)) {
            case 0:
                return false;
            case 1:
                return _es_igual(actual->get_izq(), hijo) and _es_igual(actual->get_der(), hijo);
            case 2:
                return _es_igual(actual->get_izq(), hijo) or _es_igual(actual->get_der(), hijo);
            }
        }
        return _padre(_obtener_sig(actual, padre), hijo, padre);
    }

    bool _hijo(Nodo*& actual, int padre, int hijo)
    {
        if (not actual) {
            return false;
        }
        if (actual->get_clave() == padre) {
            return _es_igual(actual->get_izq(), hijo) or _es_igual(actual->get_der(), hijo);
        }
        return _hijo(_obtener_sig(actual, padre), padre, hijo);
    }

    Nodo* _recuperar(Nodo* actual, int item)
    {
        if (not actual)
            return nullptr;
        if (actual->get_clave() == item)
            return actual;
        return _recuperar(_obtener_sig(actual, item), item);
    }

    bool _hoja(Nodo*& actual, int item)
    {
        if (not actual) {
            return false;
        }
        if (actual->get_clave() == item) {
            return _grado(actual) == 0;
        }
        return _hoja(_obtener_sig(actual, item), item);
    }

    int _altura(Nodo* actual)
    {
        if (not actual) {
            return -1;
        }
        int alt_izq = _altura(actual->get_izq());
        int alt_der = _altura(actual->get_der());
        return 1 + max(alt_izq, alt_der);
    }

    Nodo* _minimo_comun_ancestro(Nodo* actual, int item_a, int item_b)
    {
        if (not actual)
            return nullptr;

        if (actual->get_clave() > item_a and actual->get_clave() > item_b)
            return _minimo_comun_ancestro(actual->get_izq(), item_a, item_b);
        else
            return _minimo_comun_ancestro(actual->get_der(), item_a, item_b);

        return actual;
    }

    void _camino(Nodo* actual, int fin)
    {
        if (actual->get_clave() == fin) {
            cout << actual->get_clave() << " ";
            return;
        }
        cout << actual->get_clave() << " -> ";
        _camino(_obtener_sig(actual, fin), fin);
    }

    void _in_orden(Nodo* actual)
    {
        if (not actual)
            return;
        _in_orden(actual->get_izq());
        cout << actual->get_clave() << " ";
        _in_orden(actual->get_der());
    }

    void _pre_orden(Nodo* actual)
    {
        if (not actual) {
            cout << endl;
            return;
        }
        cout << actual->get_clave() << " ";
        _in_orden(actual->get_izq());
        _in_orden(actual->get_der());
    }

    void _post_orden(Nodo* actual)
    {
        if (not actual) {
            cout << endl;
            return;
        }
        _in_orden(actual->get_izq());
        _in_orden(actual->get_der());
        cout << actual->get_clave() << " ";
    }

    void _mostrar_hijo(Nodo* hijo, string pos)
    {
        if (not hijo) {
            cout << "hijo " << pos << " null";
        } else {
            cout << "hijo " << pos << hijo->get_clave();
        }
        cout << endl;
    }

    void _buscar(Nodo* actual, int item)
    {
        if (not actual)
            return;
        if (actual->get_clave() == item) {
            cout << "Nodo encontrado: " << actual->get_clave() << endl;
            _mostrar_hijo(actual->get_izq(), "izq");
            _mostrar_hijo(actual->get_der(), "der");
            return;
        }
        _buscar(_obtener_sig(actual, item), item);
    }

    Nodo* _buscar_alt(Nodo* actual, int item)
    {
        if (not actual)
            return nullptr;
        if (actual->get_clave() == item) {
            return actual;
        }
        return _buscar_alt(_obtener_sig(actual, item), item);
    }

    int _nivel(Nodo* actual, int item, int nivel = 0)
    {
        if (actual->get_clave() == item) {
            return nivel;
        }
        return _nivel(_obtener_sig(actual, item), item, nivel + 1);
    }

    void _destruir(Nodo* actual)
    {
        if (actual) {
            _destruir(actual->get_izq());
            _destruir(actual->get_der());
            delete actual;
        }
    }

public:
    Arbol() { _raiz = nullptr; }

    ~Arbol() { _destruir(_raiz); }

    void insertar(int item) { _insertar(_raiz, item); }

    void suprimir(int item) { _suprimir(_raiz, item); }

    void buscar(int item) { _buscar(_raiz, item); }
    Nodo* buscar_alt(int item) { return _buscar_alt(_raiz, item); }

    bool hoja(int item) { return _hoja(_raiz, item); }

    int altura() { return _altura(_raiz); }

    void in_orden()
    {
        _in_orden(_raiz);
        cout << endl;
    }

    void pre_orden()
    {
        _pre_orden(_raiz);
        cout << endl;
    }

    void post_orden()
    {
        _post_orden(_raiz);
        cout << endl;
    }

    bool hijo(int padre, int hijo) { return _hijo(_raiz, padre, hijo); }

    bool padre() { return _padre(_raiz, 35, 47); }

    int nivel(int item) { return _nivel(_raiz, item); }

    void camino(int inicio, int fin)
    {
        auto nodo_inicio = buscar_alt(inicio);
        if (not nodo_inicio) {
            cout << "no existe el nodo " << inicio << endl;
            return;
        }

        _camino(nodo_inicio, fin);
    }
};

int main()
{
    auto arbol = new Arbol();
    cout << "Insertando..." << endl;
    arbol->insertar(70);
    arbol->insertar(47);
    arbol->insertar(92);
    arbol->insertar(35);
    arbol->insertar(68);
    arbol->insertar(83);
    arbol->insertar(100);
    arbol->insertar(79);

    arbol->in_orden();

    arbol->suprimir(70);

    arbol->in_orden();
    return 0;
}
