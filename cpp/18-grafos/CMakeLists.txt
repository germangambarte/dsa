cmake_minimum_required(VERSION 3.10)
project(Estructuras CXX)

set(CMAKE_CXX_STANDARD 17)

# Headers
include_directories(include)

# Librería de estructuras
add_library(estructuras
    src/pila/secuencial.cpp
    src/pila/enlazada.cpp
)

# Ejercicio 1
add_executable(ejercicio1 ejercicios/ejercicio1/main.cpp)
target_link_libraries(ejercicio1 estructuras)
