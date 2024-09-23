public class Nodo
{
  public int item { get; set; }
  public Nodo? siguiente { get; set; }
}

public class Encadenada
{
  private int dimension;
  private int cantidad;
  private Nodo? tope;

  public Encadenada(int dim)
  {
    dimension = dim;
    cantidad = 0;
    tope = null;
  }

  public int Insertar(int item)
  {
    if (cantidad == dimension)
    {
      Console.WriteLine("Pila llena.");
      return -1;
    }
    Nodo nuevoNodo = new();
    nuevoNodo.item = item;
    nuevoNodo.siguiente = tope;
    tope = nuevoNodo;
    cantidad++;
    return tope.item;
  }

  public int Suprimir()
  {
    if (Vacia())
    {
      Console.WriteLine("Pilla vacia.");
      return -1;
    }
    Nodo eliminado = tope!;
    tope = tope!.siguiente;
    cantidad--;
    return eliminado!.item;
  }

  public void Recorrer()
  {
    Nodo actual = tope!;
    while (actual != null)
    {
      Console.Write(actual.item + " ");
      actual = actual.siguiente!;
    }
    Console.WriteLine();
  }

  public bool Vacia()
  {
    return cantidad == 0;
  }
}