import sys
import math

def di_hola():
    print("Di Hola")

    print("1. Muestre en la consola el siguiente string: ”Hello World”.")
    print("Hello World!")

    print("2. Muestre en la consola el valor m´aximo y el valor m´ ınimo admitidos por el tipo int.")
    print(f'El valor máximo de int es: {sys.maxsize}')
    print(f'El valor mínimo de int es: {-sys.maxsize - 1}')

    print("3. Muestre en la consola un valor aproximado de Pi (use Math).")
    print(f'El valor aproximado de Pi es: {math.pi}')

    print("Recibiendo entradas")

def recibiendo_entradas():
    print("1. Reciba como entrada una cadena de caracteres (string). Luego muestre en la terminal ese mismo string pero con terminación ”medio limón”.")


    print("2. Reciba un número y muestre en la consola su doble.")
    print("Deme un numero")
    a = input()
    a = int(a)
    print(a *2)

    print(" 3. Reciba tres números. Muestre en consola el menor y el mayor de estos.")
    a = int(input())
    b = int(input())
    c = int(input())
    print(min(a, b, c), max(a, b, c))
    print(min(a,min(b,c)))
    print(max(a,max(b,c)))


    print("ej 4")
    a = int(input())
    b = int(input())
    c = int(input())
    print()
    print((a + b + c)//2)


    a = 3
    a = 2*a
    print(a)

    print(int(input("deme un numero")) * 2)

    #juego con operadores y orden
    a = 5
    b = a + 1
    print(b)

    a = 10
    b = 2
    resultado = a > b
    print(resultado)

    nombre = input("Como te llamas ")
    print("Hola " + (nombre + " ") * 3)

    edad_str = input("que edad tienes ")
    edad_num = int(edad_str)
    print("El año que viene tendrás", edad_num + 1)

def hanoi_towers():
    print("Introduce las cantidad de aros")
    rings = int(input())
    print("La menor cantidad de pasos es", pow(2,rings) - 1)

def max_min_3num():
    a = int(input())
    b = int(input())
    c = int(input())


def max_min():
    a = int(input())
    b = int(input())
    c = int(input())

#TODO: hacer lo del max y min con operadores aritmeticos y logicos


