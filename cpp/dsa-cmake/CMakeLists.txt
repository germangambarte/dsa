cmake_minimum_required(VERSION 3.10)
project(DSAProject)

set(CMAKE_CXX_STANDARD 17)

# Incluir headers
include_directories(include)

# Librería de estructuras
add_library(dsastructs
    src/PilaSecuencial.cpp
    src/PilaEnlazada.cpp
    src/ColaSecuencial.cpp
    src/ColaEnlazada.cpp
    src/ColaCircular.cpp
    src/Nodo.cpp
)

# Ejecutable de prueba
add_executable(pila_secuencial
    tests/pila-secuencial/main.cpp
)

add_executable(pila_enlazada
    tests/pila-secuencial/main.cpp
)

add_executable(cola_secuencial
    tests/cola-secuencial/main.cpp
)

add_executable(cola_enlazada
    tests/cola-enlazada/main.cpp
)

add_executable(cola_circular
    tests/cola-circular/main.cpp
)

# Enlazar ejecutable con la librería
target_link_libraries(pila_secuencial dsastructs)
target_link_libraries(pila_enlazada dsastructs)
target_link_libraries(cola_secuencial dsastructs)
target_link_libraries(cola_enlazada dsastructs)
target_link_libraries(cola_circular dsastructs)
