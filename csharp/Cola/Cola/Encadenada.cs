class Nodo
{
  public int Item { get; set; }
  public Nodo? Siguiente { get; set; }
}

namespace Cola
{
  class Encadenada(int dim)
  {
    private readonly int dimension = dim;
    private int cantidad = 0;
    private Nodo? ultimo = null;
    private Nodo? primero = null;

    public int Insertar(int item)
    {
      if (cantidad == dimension)
      {
        Console.WriteLine("Cola llena.");
        return -1;
      }
      Nodo nuevoNodo = new()
      {
        Item = item,
        Siguiente = null
      };
      if (ultimo == null)
      {
        primero = nuevoNodo;
      }
      else
      {
        ultimo.Siguiente = nuevoNodo;
      }
      ultimo = nuevoNodo;
      cantidad++;
      return item;
    }

    public int Suprimir()
    {
      if (Vacia())
      {
        Console.WriteLine("Cola vacia.");
        return -1;
      }
      Nodo eliminado = primero!;
      primero = primero!.Siguiente;
      cantidad--;
      return eliminado.Item;
    }

    public void Recorrer()
    {
      Nodo actual = primero!;
      while (actual != null)
      {
        Console.Write(actual!.Item + " ");
        actual = actual!.Siguiente!;
      }
      Console.WriteLine();
    }

    public bool Vacia()
    {
      return cantidad == 0;
    }
  }
}