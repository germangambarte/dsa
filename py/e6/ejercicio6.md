Para resolver el Ejercicio Nº 6 usando la clase `Cola` que tienes, es necesario realizar algunas modificaciones para adaptarla a las necesidades de la simulación y luego crear una función que simule el comportamiento de la impresora.

### Modificaciones en la clase `Cola`

La clase `Cola` actual es más parecida a una pila debido a que los elementos se insertan y eliminan desde la cabeza. Para transformarla en una cola verdadera, donde los elementos se insertan en un extremo (final) y se eliminan desde el otro (frente), se deben realizar algunos ajustes:

1. **Agregar un puntero al final**: Para que las inserciones se realicen en el final de la cola.
2. **Modificar el método `insertar`**: Para que inserte elementos al final de la cola.

Aquí tienes la versión ajustada de la clase `Cola`:

```c++
#include <iostream>

class Nodo {
public:
  int item;
  Nodo *siguiente;

  Nodo(int valor) : item(valor), siguiente(nullptr) {}
};

class Cola {
private:
  Nodo *cabeza;
  Nodo *cola;
  int cantidad;

public:
  Cola() : cabeza(nullptr), cola(nullptr), cantidad(0) {}

  ~Cola() {
    while (!vacia()) {
      suprimir();
    }
  }

  void insertar(int item) {
    Nodo *nuevoNodo = new Nodo(item);
    if (vacia()) {
      cabeza = cola = nuevoNodo;
    } else {
      cola->siguiente = nuevoNodo;
      cola = nuevoNodo;
    }
    cantidad++;
  }

  void suprimir() {
    if (vacia()) {
      std::cout << "Cola vacía." << std::endl;
    } else {
      Nodo *nodoAEliminar = cabeza;
      cabeza = cabeza->siguiente;
      delete nodoAEliminar;
      cantidad--;
      if (cabeza == nullptr) {
        cola = nullptr;
      }
    }
  }

  int obtenerFrente() {
    if (vacia()) {
      std::cout << "Cola vacía." << std::endl;
      return -1;  // Indica que la cola está vacía
    }
    return cabeza->item;
  }

  bool vacia() { return cantidad == 0; }
};

```

### Simulación de la cola de impresión

Ahora vamos a implementar la función que simula el comportamiento de la cola de impresión.

#### Implementación de la simulación:

```c++
#include <iostream>

class Nodo {
public:
  int item;
  Nodo *siguiente;

  Nodo(int valor) : item(valor), siguiente(nullptr) {}
};

class Cola {
private:
  Nodo *cabeza;
  Nodo *cola;
  int cantidad;

public:
  Cola() : cabeza(nullptr), cola(nullptr), cantidad(0) {}

  ~Cola() {
    while (!vacia()) {
      suprimir();
    }
  }

  void insertar(int item) {
    Nodo *nuevoNodo = new Nodo(item);
    if (vacia()) {
      cabeza = cola = nuevoNodo;
    } else {
      cola->siguiente = nuevoNodo;
      cola = nuevoNodo;
    }
    cantidad++;
  }

  void suprimir() {
    if (vacia()) {
      std::cout << "Cola vacía." << std::endl;
    } else {
      Nodo *nodoAEliminar = cabeza;
      cabeza = cabeza->siguiente;
      delete nodoAEliminar;
      cantidad--;
      if (cabeza == nullptr) {
        cola = nullptr;
      }
    }
  }

  int obtenerFrente() {
    if (vacia()) {
      std::cout << "Cola vacía." << std::endl;
      return -1;  // Indica que la cola está vacía
    }
    return cabeza->item;
  }

  bool vacia() { return cantidad == 0; }
  int tamano() { return cantidad; }
};

void simulacionImpresion(int tiempoSimulacion, int intervaloLlegada, int tiempoMaxProceso) {
  Cola colaImpresion;
  int tiempoActual = 0;
  int trabajosNoAtendidos = 0;
  int totalTrabajos = 0;
  int totalTiempoEspera = 0;

  // Generar trabajos de impresión cada intervaloLlegada minutos
  for (int i = 0; i < tiempoSimulacion; i += intervaloLlegada) {
    int tiempoTrabajo = rand() % 10 + 1; // Tiempo de impresión aleatorio entre 1 y 10 minutos
    colaImpresion.insertar(tiempoTrabajo);
    totalTrabajos++;
  }

  while (tiempoActual < tiempoSimulacion) {
    if (!colaImpresion.vacia()) {
      int tiempoRestante = colaImpresion.obtenerFrente();

      if (tiempoRestante <= tiempoMaxProceso) {
        tiempoActual += tiempoRestante;
        totalTiempoEspera += tiempoActual;
        colaImpresion.suprimir();
      } else {
        tiempoActual += tiempoMaxProceso;
        colaImpresion.suprimir();
        colaImpresion.insertar(tiempoRestante - tiempoMaxProceso);
      }
    } else {
      tiempoActual += intervaloLlegada;
    }
  }

  trabajosNoAtendidos = colaImpresion.tamano();
  double promedioEspera = totalTrabajos > 0 ? static_cast<double>(totalTiempoEspera) / totalTrabajos : 0;

  std::cout << "Trabajos sin atender: " << trabajosNoAtendidos << std::endl;
  std::cout << "Promedio de espera: " << promedioEspera << " minutos" << std::endl;
}

int main() {
  int tiempoSimulacion = 60;  // Simulación de 1 hora (60 minutos)
  int intervaloLlegada = 5;   // Los trabajos llegan cada 5 minutos
  int tiempoMaxProceso = 5;   // Tiempo máximo para procesar cada trabajo

  simulacionImpresion(tiempoSimulacion, intervaloLlegada, tiempoMaxProceso);

  return 0;
}

```

### Explicación del código:

1. **Cola de impresión (`Cola`)**: Esta cola se utiliza para manejar los trabajos de impresión, donde cada trabajo tiene un tiempo de procesamiento aleatorio entre 1 y 10 minutos.

2. **Función `simulacionImpresion`**:

   - **Parámetros**:
     - `tiempoSimulacion`: Duración total de la simulación.
     - `intervaloLlegada`: Intervalo en minutos entre la llegada de cada trabajo.
     - `tiempoMaxProceso`: Tiempo máximo que la impresora puede dedicar a un trabajo antes de moverlo al final de la cola si no se ha terminado.
   - **Lógica**:
     - Se generan trabajos de impresión con tiempos de procesamiento aleatorios y se añaden a la cola.
     - La impresora procesa los trabajos, quitando el tiempo correspondiente de cada uno. Si un trabajo no se puede terminar en 5 minutos, se coloca de nuevo en la cola con el tiempo restante.
     - Se calculan la cantidad de trabajos sin atender y el tiempo promedio de espera.

3. **Resultado**:
   - Se imprime la cantidad de trabajos que quedaron sin atender después de la simulación.
   - Se calcula el promedio de espera de los trabajos que fueron atendidos.

Esta simulación debería cumplir con los requisitos del ejercicio y ayudarte a entender cómo funciona una cola en un entorno de simulación de procesos.
