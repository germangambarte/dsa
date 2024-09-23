import { PilaSecuencial } from "./src/pila-secuencial.ts";
import { PilaEncadenada } from "./src/pila-encadenada.ts";

if (import.meta.main) {
  // let pila: PilaSecuencial = new PilaSecuencial(4);
  let pila: PilaEncadenada = new PilaEncadenada(4);

  pila.insertar(1);
  pila.insertar(2);
  pila.insertar(3);
  pila.insertar(4);
  pila.insertar(5);

  pila.recorrer();

  pila.suprimir();
  pila.suprimir();

  pila.recorrer();
}
