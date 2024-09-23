export class PilaSecuencial {
  private items: number[];
  private dimension: number;
  private cantidad: number;
  private tope: number;

  constructor(dimension: number) {
    this.dimension = dimension;
    this.cantidad = 0;
    this.tope = -1;
    this.items = [];
  }

  insertar(item: number): number {
    if (this.cantidad == this.dimension) {
      console.log("Pila llena.");
      return -1;
    }
    this.items[++this.tope] = item;
    this.cantidad++;
    return item;
  }

  suprimir(): number {
    if (this.vacia()) {
      console.log("Pila vacia.");
      return -1;
    }
    this.cantidad--;
    return this.items[this.tope--];
  }

  recorrer() {
    if (this.vacia()) {
      console.log("Pila vacia.");
      return;
    }
    let pila: number[] = [];
    for (let i = this.tope; i > -1; i--) {
      pila.push(this.items[i]);
    }
    console.log(pila);
  }

  vacia(): boolean {
    return this.cantidad == 0;
  }
}
