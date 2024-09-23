namespace Cola
{

  class Secuencial(int dim)
  {
    private readonly int[] items = new int[dim];
    private readonly int dimension = dim;
    private int cantidad = 0;
    private int ultimo = 0;
    private int primero = 0;

    public int Insertar(int item)
    {
      if (cantidad == dimension)
      {
        Console.WriteLine("Cola llena");
        return -1;
      }
      items[ultimo] = item;
      ultimo = (ultimo + 1) % dimension;
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
      int eliminado = items[primero];
      primero = (primero + 1) % dimension;
      cantidad--;
      return eliminado;
    }

    public void Recorrer()
    {
      for (int i = primero, j = 0; j < cantidad; i = (i + 1) % dimension, j++)
      {
        Console.Write(items[i] + " ");
      }
      Console.WriteLine();
    }

    public bool Vacia()
    {
      return cantidad == 0;
    }
  }
}