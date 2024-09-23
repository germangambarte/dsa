class Nodo {
  private _item: number;
  private _siguiente: Nodo | null;

  get item() {
    return this._item;
  }

  get siguiente() {
    return this._siguiente;
  }

  set item(item: number) {
    this._item = item;
  }

  set siguiente(siguiente: Nodo | null) {
    this._siguiente = siguiente;
  }
}

export class PilaEncadenada {
  private dimension: number;
  private cantidad: number;
  private tope: Nodo | null;

  constructor(dimension: number) {
    this.dimension = dimension;
    this.cantidad = 0;
    this.tope = null;
  }

  insertar(item: number): number {
    if (this.cantidad == this.dimension) {
      console.log("Pila llena.");
      return -1;
    }
    let nuevoNodo = new Nodo();
    nuevoNodo.item = item;
    nuevoNodo.siguiente = this.tope;
    this.tope = nuevoNodo;
    this.cantidad++;
    return this.tope.item;
  }

  suprimir(): number | null {
    if (this.vacia()) {
      console.log("Pila vacia.");
      return null;
    }
    let eliminado = this.tope;
    this.tope = this.tope!.siguiente;
    this.cantidad--;
    return eliminado!.item;
  }

  recorrer(): void {
    let actual = this.tope;
    let pila: number[] = [];
    while (actual != null) {
      pila.push(actual.item);
      actual = actual!.siguiente;
    }
    console.log(pila);
  }

  vacia(): boolean {
    return this.cantidad == 0;
  }
}
