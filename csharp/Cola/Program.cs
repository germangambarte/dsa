using Cola;

// Secuencial cola = new(4);
Encadenada cola = new(4);

cola.Insertar(1);
cola.Insertar(2);
cola.Insertar(3);
cola.Insertar(4);
cola.Insertar(5);

cola.Recorrer();

cola.Suprimir();
cola.Suprimir();

cola.Recorrer();