import sys
import math

def di_hola():
    print("Hello World!")

    print(f'El valor máximo de int es: {sys.maxsize}')
    print(f'El valor mínimo de int es: {-sys.maxsize - 1}')

    print(f'El valor aproximado de Pi es: {math.pi}')


def recibiendo_entradas():

    print("Deme un numero")
    a = input()
    a = int(a)
    print(a * 2)

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
def max_min():
    a = int(input("numero 1\n"))
    b = int(input("numero 2\n"))
    c = int(input("numero 3\n"))
    if a > b and a > c:
        print(f"{a} es el mayor")
    if b > a and b > c:
        print(f"{b} es el mayor")
    if c > a and c > b:
        print(f"{c} es el mayor")
    else:
        print("son iguales")
# done!

max_min()

