using System.Globalization;

namespace Lista
{
  class Secuencial(int dim)
  {
    private readonly int Dimension = dim;
    private int Cantidad = 0;
    private int[] Items = new int[dim];
    private int Ultimo = -1;

    public int InsertarContenido(int item)
    {
      if (Cantidad == Dimension)
      {
        Console.WriteLine("Lista llena");
        return -1;
      }
      int i = 0;
      while (i <= Ultimo && Items[i] < item)
      {
        i++;
      }
      for (int j = Ultimo; j > i; j--)
      {
        Items[j] = Items[j - 1];
      }
      Items[i] = item;
      Cantidad++;
      Ultimo++;
      return Items[i];
    }

    public int InsertarPosicion(int item, int posicion)
    {
      if (Cantidad == Dimension)
      {
        Console.WriteLine("Lista llena");
        return -1;
      }
      if (0 <= posicion && posicion <= Ultimo)
      {
        int i = Ultimo + 1;
        while (i > posicion)
        {
          Items[i] = Items[i - 1];
          i--;
        }
        Items[posicion] = item;
        Cantidad++;
        Ultimo++;
        return Items[posicion];
      }
      Console.WriteLine("Posicion no valida");
      return -1;
    }

    public int SuprimirContenido(int item)
    {
      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      int i = 0;
      while (i <= Ultimo && Items[i] == item)
      {
        i++;
      }
      if (Items[i] != item)
      {
        Console.WriteLine("Item no valido");
        return -1;
      }
      int eliminado = Items[i];
      for (int j = i; j <= Ultimo; j++)
      {
        Items[j] = Items[j + 1];
      }
      Cantidad--;
      Ultimo--;
      return eliminado;
    }

    public int SuprimirPosicion(int posicion)
    {
      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      if (0 <= posicion && posicion <= Ultimo)
      {
        int eliminado = Items[posicion];
        while (posicion <= Ultimo)
        {
          Items[posicion] = Items[posicion++];
        }
        Cantidad--;
        Ultimo--;
        return eliminado;
      }
      Console.WriteLine("Posicion no valida");
      return -1;
    }

    public int Buscar(int item)
    {
      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      int i = 0;
      while (i <= Ultimo && Items[i] != item)
      {
        i++;
      }
      if (Items[i] == item)
      {
        return item;
      }
      Console.WriteLine("Elemento no valido");
      return -1;
    }

    public void Recorrer()
    {
      for (int i = 0; i < Cantidad; i++)
      {
        Console.Write(Items[i] + " ");
      }
      Console.WriteLine();
    }

    public int PrimerElemento()
    {
      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      return Items[0];
    }

    public int UltimoElemento()
    {
      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      return Items[Ultimo];
    }

    public int Siguiente(int posicion)
    {

      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      if (posicion == Ultimo)
      {
        Console.WriteLine("Ingreso la ultima posicion");
        return -1;
      }
      return Items[posicion + 1];
    }

    public int Anterior(int posicion)
    {

      if (Vacia())
      {
        Console.WriteLine("Lista vacia.");
        return -1;
      }
      if (posicion == 0)
      {
        Console.WriteLine("Ingreso la primera posicion");
        return -1;
      }
      return Items[posicion - 1];
    }

    public bool Vacia()
    {
      return Cantidad == 0;
    }

    public bool Llena()
    {
      return Cantidad == Dimension;
    }
  }

}