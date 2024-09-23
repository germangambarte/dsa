void conversionBinaria(int valor) {
  PilaSecuencial pila(3);

  int valorActual = valor;
  while (valorActual >= 2) {
    pila.insertar(valorActual % 2);
    valorActual /= 2;
  }
  pila.insertar(valorActual % 2);

  std::cout << "binario: ";
  while (!pila.vacia()) {
    std::cout << pila.suprimir() << "";
  }
  std::cout << std::endl;
}

int main() {
  conversionBinaria(12345);
  return 0;
}
