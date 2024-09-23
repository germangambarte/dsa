export class ColaSecuencial {
  private items: number[];
  private dimension: number;
  private cantidad: number;
  private ultimo: number;
  private primero: number;

  constructor(dimension: number) {
    this.dimension = dimension;
    this.cantidad = 0;
    this.ultimo = 0;
    this.primero = 0;
    this.items = [];
  }

  insertar(item: number): number {
    if (this.cantidad == this.dimension) {
      console.log("Cola llena.");
      return -1;
    }

    this.items[this.ultimo] = item;
    this.ultimo = (this.ultimo + 1) % this.dimension;
    this.cantidad++;
    return item;
  }

  suprimir(): number {
    if (this.vacia()) {
      console.log("Cola vacia.");
      return -1;
    }
    let eliminado = this.items[this.primero];
    this.primero = (this.primero + 1) % this.dimension;
    return eliminado;
  }

  recorrer() {
    if (this.vacia()) {
      console.log("Cola vacia.");
      return;
    }
    let cola: number[] = [];
    let i = this.primero;
    for (let j = this.ultimo; i > -1; i--) {
      cola.push(this.items[i]);
    }
    console.log(cola);
  }

  vacia(): boolean {
    return this.cantidad == 0;
  }
}
