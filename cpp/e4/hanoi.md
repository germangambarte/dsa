Para implementar el juego de las Torres de Hanoi en C++, podemos utilizar la clase
`Pila` que ya tienes, y añadir algunas funciones para manejar la lógica del juego.
Aquí te muestro una posible implementación:

1. **Modificar la clase `Pila`:** Agregar métodos para obtener el elemento en la
   cima (sin eliminarlo) y para comprobar si un movimiento es válido.
2. **Agregar la lógica del juego en el `main`:** Inicializar las pilas y manejar
   la entrada del usuario para mover discos entre las pilas.

### Modificación de la clase `Pila`

Primero, vamos a agregar un método para obtener el tope de la pila sin eliminarlo:

```c++
int cima() {
  if (!vacia()) {
    return items[tope - 1];
  } else {
    return -1; // Valor que indica que la pila está vacía
  }
}
```

### Implementación del juego en `main`

```c++
#include <iostream>
#include <vector>

class Pila {
private:
  std::vector<int> items;
  int cantidad;
  int tope;
  int dimension;

public:
  Pila(int dim) : cantidad(0), tope(0), dimension(dim) {
    items.resize(dimension);
  }

  void insertar(int item) {
    if (cantidad == dimension) {
      dimension += 5;
      items.resize(dimension);
    }

    items[tope] = item;
    tope++;
    cantidad++;
  }

  int suprimir() {
    if (vacia()) {
      std::cout << "Pila vacía." << std::endl;
      return -1; // Devuelve -1 si está vacía
    } else {
      tope--;
      cantidad--;
      return items[tope];
    }
  }

  int cima() {
    if (!vacia()) {
      return items[tope - 1];
    } else {
      return -1;
    }
  }

  void recorrer() {
    for (int i = tope - 1; i >= 0; i--) {
      std::cout << items[i] << " ";
    }
    std::cout << std::endl;
  }

  bool vacia() { return cantidad == 0; }
};

void mostrarEstado(Pila &p1, Pila &p2, Pila &p3) {
  std::cout << "Pila 1: ";
  p1.recorrer();
  std::cout << "Pila 2: ";
  p2.recorrer();
  std::cout << "Pila 3: ";
  p3.recorrer();
}

bool moverDisco(Pila &origen, Pila &destino) {
  int discoOrigen = origen.cima();
  int discoDestino = destino.cima();

  if (discoOrigen == -1) {
    std::cout << "Movimiento no permitido: la pila origen está vacía." << std::endl;
    return false;
  }

  if (discoDestino == -1 || discoOrigen < discoDestino) {
    destino.insertar(origen.suprimir());
    return true;
  } else {
    std::cout << "Movimiento no permitido: no se puede poner un disco más grande sobre uno más pequeño." << std::endl;
    return false;
  }
}

int main() {
  int n;
  std::cout << "Ingrese el número de discos: ";
  std::cin >> n;

  Pila p1(n), p2(n), p3(n);

  // Colocar todos los discos en la primera pila
  for (int i = n; i >= 1; i--) {
    p1.insertar(i);
  }

  mostrarEstado(p1, p2, p3);

  int origen, destino;
  int jugadas = 0;
  int jugadasMinimas = (1 << n) - 1; // 2^n - 1

  while (!(p1.vacia() && p2.vacia())) {
    std::cout << "Ingrese la pila origen y destino (1, 2 o 3): ";
    std::cin >> origen >> destino;

    Pila *pilaOrigen, *pilaDestino;

    if (origen == 1) pilaOrigen = &p1;
    else if (origen == 2) pilaOrigen = &p2;
    else pilaOrigen = &p3;

    if (destino == 1) pilaDestino = &p1;
    else if (destino == 2) pilaDestino = &p2;
    else pilaDestino = &p3;

    if (moverDisco(*pilaOrigen, *pilaDestino)) {
      jugadas++;
      mostrarEstado(p1, p2, p3);
    }
  }

  std::cout << "Juego terminado en " << jugadas << " jugadas." << std::endl;
  std::cout << "El número mínimo de jugadas es " << jugadasMinimas << "." << std::endl;

  return 0;
}
```

### Descripción del Código

1. **Clase `Pila`:** Se ha agregado un método `cima()` para obtener el elemento
   en la cima sin quitarlo.
2. **Función `moverDisco`:** Mueve un disco de una pila a otra si el movimiento es válido.
3. **Función `mostrarEstado`:** Imprime el estado actual de las tres pilas.
4. **Lógica del juego:** En el `main`, se inicializan las pilas, se colocan los
   discos en la pila 1, y se maneja la lógica del juego hasta que todos los discos estén en la pila 3.

Este código implementa el juego según las reglas descritas. Cada movimiento es
validado antes de realizarse, asegurando que no se viole ninguna de las reglas del juego.
