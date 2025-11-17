class Program
{
    public static void Main()
    {
        //Acá el método Bucle que habías declarado es innecesario, ya está dentro de Main el while 
        while (true) //!https://es.wikipedia.org/wiki/True_y_false  
        {
            if (Console.ReadLine() == "x") //No puede ser Console.WriteLine("x") porque eso imprime una x en la consola
            {
                break; 
            }

            Ej02();
            Ej03();
            Ej04();
            Ej05();
            Ej06();
            Ej07();
            Ej08();

        }
    }
    public static void Ej02()
    {
        Console.WriteLine("El valor mínimo admitido por el tipo int es " + int.MinValue);
        Console.WriteLine("El valor máximo admitido por el tipo int es " + int.MaxValue);
        Console.WriteLine($"Valor mínimo de int con interpolación de cadenas {int.MinValue}");
    }
    public static void Ej03()
    {
        Console.WriteLine("Valor aproximado de PI: " + Math.PI);
    }
    public static void Ej04()
    {
        Console.WriteLine("Introduce un string para hacerlo terminar en medio limón");
        Console.WriteLine(Console.ReadLine() + " medio limón");
    }
    public static void Ej05()
    {
        Console.WriteLine("Introduce un numero para calcular el doble");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine(2 * a);
    }


    /// <summary>
    /// Reciba dos números enteros de la consola 
    /// y determine cual de los dos es mayor sin utilizar Math.Max y Math.Min.
    /// </summary>
    public static void Ej06()
    {
        Console.WriteLine("Introduce dos numeros para compararlos");
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());

        if (a == b)
        {
            Console.WriteLine("Los números son iguales");
        }

        if (a > b)
        {
            Console.WriteLine(a + " es mayor que " + b);
        }

        if (a < b)
        {
            Console.WriteLine(a + " es menor que " + b);
        }

        //Usando else if
        if (a > b) Console.WriteLine(a + " es mayor que " + b);
        else if (a < b) Console.WriteLine(b + " es mayor que " + a);
        else Console.WriteLine("Los números son iguales");

        //Usando Math.Min y Math.Max
        if (a == b) Console.WriteLine("Son iguales");
        else Console.WriteLine("El número mayor es " + Math.Max(a, b));


    }


    /// <summary>
    ///Reciba tres números enteros. Muestre en la consola el de valor medio (Utilice Math.Max y Math.Min) 
    ///y el promedio de estos.
    /// </summary>
    public static void Ej07()
    {
        Console.WriteLine("Ingresa 3 números enteros");
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());
        int c = int.Parse(Console.ReadLine());


    }

    /// <summary>
    ///Reciba un string y un entero (x) menor que el total de caracteres del string. 
    ///Muestre en la consola el caracter que ocupa la posición x en el string
    /// </summary>
    public static void Ej08()
    {
        Console.WriteLine("Ingrese un string y un entero menor que la cantidad de caracteres del string");
        string str = Console.ReadLine();

        while (true)
        {
            int entero = int.Parse(Console.ReadLine());

            if (entero >= str.Length)
            {
                Console.WriteLine("Por favor ingrese un entero menor que la cantidad de caracteres del string");
            }
            else 
            {
                Console.WriteLine(str[entero]);
                break;
            }

        }

    }
}
