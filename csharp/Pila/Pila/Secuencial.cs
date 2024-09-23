using System;

namespace Pila;

public class Secuencial
{
  private int dimension;
  private int cantidad;
  private int tope;
  private int[] items;

  public Secuencial(int dim)
  {
    dimension = dim;
    cantidad = 0;
    tope = -1;
    items = new int[dim];
  }

  public int Insertar(int item)
  {
    if (cantidad == dimension)
    {
      Console.WriteLine("Pila llena.");
      return -1;
    }

    items[++tope] = item;
    cantidad++;
    return item;
  }

  public int Suprimir()
  {
    if (Vacia())
    {
      Console.WriteLine("Pila vacia.");
      return -1;
    }
    cantidad--;
    return items[tope--];
  }

  public void Recorrer()
  {
    if (Vacia())
    {
      Console.WriteLine("Pila vacia.");
      return;
    }
    for (int i = tope; i >= 0; i--)
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
