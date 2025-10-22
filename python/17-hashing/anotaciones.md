# Direccionamiento abierto
[] Dimensionar el arreglo:
    tamaño del arreglo:
        - M = número primo > N/0.7
[] función hash
    - la funcion de has puede ser cualquiera de las vistas
[] Secuencia de prueba
    - Aplicar función de prueba en caso de coliciones:
    - Si el lugar está ocupado busco el siguiente libre
[] Busqueda:
    - Si me encuentro con una celda vacia, el elemento no está guardado
    - De lo contrario el elemento existe
_____________
|_____x_____|
|___________|
|_____x_____|
|_____x_____|
|___________|
|_____x_____|
# Encadenamiento (arreglo de pilas encandenadas)
- Si tengo una colisión lo inserto en una lista encadenada que inserta por cabeza (una pila encadenada con un método buscar)
- Dimension del arreglo:
    - determinar número máximo de coliciones
    - luego, M = N/cantidad de coliciones esperadas

+-----------+
|  |  x  |  | -> |  y  | -> |   z  |
+-----------+
+-----------+
|  |  a  |  | -> |  b  | -> |   c  |
+-----------+
+-----------+
|           |
+-----------+
+-----------+
|  |  m  |  | -> |  n  | -> |   o  |
+-----------+
# Buckets
- Es un arreglo de arreglos
- El arreglo contenido en el bucket tiene tamaño C
- Una vez que el arreglo alcanza el tamaño C, el siguiente elemento ingresado se guarda en el area de overflow
- Area de overflow:
    - tamaño: M = N/ tamaño bucket
    - los elementos se guardan en el primero lugar libre
