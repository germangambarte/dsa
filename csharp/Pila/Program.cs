using Pila;

// Secuencial pila = new(4);
Encadenada pila = new(4);

pila.Insertar(1);
pila.Insertar(2);
pila.Insertar(3);
pila.Insertar(4);
pila.Insertar(5);

pila.Recorrer();

pila.Suprimir();
pila.Suprimir();

pila.Recorrer();