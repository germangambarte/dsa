Para resolver este problema de simulación en el banco con 3 cajeros, puedes adaptar la clase `Cola` que has creado para representar las colas de clientes en cada cajero. Luego, implementaremos una simulación para determinar las métricas solicitadas.

### Paso 1: Modificar la clase `Cola`

La clase `Cola` que ya tienes puede utilizarse para representar la fila de clientes que esperan en cada cajero. No necesitas realizar cambios significativos en ella.

### Paso 2: Implementar la simulación

La simulación se llevará a cabo en función del tiempo, donde simularemos el proceso de atención de clientes durante 2 horas. Aquí está el código que resuelve el problema:

```c++
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <queue>

class Cliente {
public:
    int tiempoLlegada;
    int tiempoAtencion;

    Cliente(int llegada, int atencion)
        : tiempoLlegada(llegada), tiempoAtencion(atencion) {}
};

int main() {
    const int tiempoSimulacion = 120; // 2 horas en minutos
    const int tiempoLlegadaPromedio = 2; // Los clientes llegan cada 2 minutos en promedio
    const int tiempoAtencionCajero1 = 5; // Cajero 1: 5 minutos
    const int tiempoAtencionCajero2 = 3; // Cajero 2: 3 minutos
    const int tiempoAtencionCajero3 = 4; // Cajero 3: 4 minutos

    std::queue<Cliente> colaCajero1, colaCajero2, colaCajero3;

    int tiempoActual = 0;
    int clientesAtendidos = 0;
    int clientesNoAtendidos = 0;
    int tiempoMaxEspera = 0;
    int sumaTiemposEspera = 0;
    int sumaTiemposEsperaNoAtendidos = 0;

    std::srand(std::time(0)); // Semilla para la aleatoriedad

    while (tiempoActual < tiempoSimulacion) {
        // Llegada de un nuevo cliente
        if (tiempoActual % tiempoLlegadaPromedio == 0) {
            Cliente nuevoCliente(tiempoActual, 0);
            // Determinar a qué cola va el cliente
            if (colaCajero1.size() <= colaCajero2.size() && colaCajero1.size() <= colaCajero3.size()) {
                nuevoCliente.tiempoAtencion = tiempoAtencionCajero1;
                colaCajero1.push(nuevoCliente);
            } else if (colaCajero2.size() <= colaCajero1.size() && colaCajero2.size() <= colaCajero3.size()) {
                nuevoCliente.tiempoAtencion = tiempoAtencionCajero2;
                colaCajero2.push(nuevoCliente);
            } else {
                nuevoCliente.tiempoAtencion = tiempoAtencionCajero3;
                colaCajero3.push(nuevoCliente);
            }
        }

        // Atender clientes en cada cajero
        if (!colaCajero1.empty()) {
            Cliente &frente = colaCajero1.front();
            if (tiempoActual - frente.tiempoLlegada >= frente.tiempoAtencion) {
                int tiempoEspera = tiempoActual - frente.tiempoLlegada;
                tiempoMaxEspera = std::max(tiempoMaxEspera, tiempoEspera);
                sumaTiemposEspera += tiempoEspera;
                colaCajero1.pop();
                clientesAtendidos++;
            }
        }

        if (!colaCajero2.empty()) {
            Cliente &frente = colaCajero2.front();
            if (tiempoActual - frente.tiempoLlegada >= frente.tiempoAtencion) {
                int tiempoEspera = tiempoActual - frente.tiempoLlegada;
                tiempoMaxEspera = std::max(tiempoMaxEspera, tiempoEspera);
                sumaTiemposEspera += tiempoEspera;
                colaCajero2.pop();
                clientesAtendidos++;
            }
        }

        if (!colaCajero3.empty()) {
            Cliente &frente = colaCajero3.front();
            if (tiempoActual - frente.tiempoLlegada >= frente.tiempoAtencion) {
                int tiempoEspera = tiempoActual - frente.tiempoLlegada;
                tiempoMaxEspera = std::max(tiempoMaxEspera, tiempoEspera);
                sumaTiemposEspera += tiempoEspera;
                colaCajero3.pop();
                clientesAtendidos++;
            }
        }

        tiempoActual++;
    }

    // Contar los clientes que no fueron atendidos
    clientesNoAtendidos = colaCajero1.size() + colaCajero2.size() + colaCajero3.size();
    sumaTiemposEsperaNoAtendidos += clientesNoAtendidos * tiempoSimulacion;

    double promedioEspera = clientesAtendidos > 0 ? static_cast<double>(sumaTiemposEspera) / clientesAtendidos : 0;
    double promedioEsperaNoAtendidos = clientesNoAtendidos > 0 ? static_cast<double>(sumaTiemposEsperaNoAtendidos) / clientesNoAtendidos : 0;

    // Resultados
    std::cout << "Tiempo máximo de espera: " << tiempoMaxEspera << " minutos" << std::endl;
    std::cout << "Cantidad de clientes atendidos: " << clientesAtendidos << std::endl;
    std::cout << "Cantidad de clientes que quedaron sin atender: " << clientesNoAtendidos << std::endl;
    std::cout << "Promedio de espera de los clientes atendidos: " << promedioEspera << " minutos" << std::endl;
    std::cout << "Promedio de espera de los clientes sin atender: " << promedioEsperaNoAtendidos << " minutos" << std::endl;

    return 0;
}
```

### Explicación del código:

1. **Clases y estructura**:

   - **Cliente**: Clase que representa un cliente con su tiempo de llegada y tiempo de atención.
   - **Colas de cajeros**: Usamos `std::queue` para simular la cola de cada cajero.

2. **Simulación**:

   - **Llegada de clientes**: Cada cliente llega cada 2 minutos en promedio y es asignado a la cola más corta.
   - **Atención de clientes**: Cada cajero atiende a su cliente en la cabeza de la cola. Si el tiempo de atención se ha completado, el cliente es retirado de la cola y se cuenta como atendido.
   - **Medición de tiempos**: Se calculan los tiempos de espera para los clientes atendidos y no atendidos.

3. **Resultados**:
   - Se imprime el tiempo máximo de espera, la cantidad de clientes atendidos y no atendidos, así como los promedios de espera para ambos grupos.

Este código te permitirá simular el proceso de atención en el banco y obtener las métricas solicitadas.
