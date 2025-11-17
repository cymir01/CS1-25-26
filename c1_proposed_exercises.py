def quadratic_calculator():
    a = int(input("introduce a \n"))
    b = int(input("introduce b \n"))
    c = int(input("introduce c \n"))

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("the ecuation has no real roots")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"there's only one real solution: {x}")
    else:
        x1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
        x2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
        print(f"the roots of the ecuation are: \nx1 = {x1}, x2 = {x2}")


def triangular_inequality():
    a = int(input("enter a\n"))
    b = int(input("enter b\n"))
    c = int(input("enter c\n"))
    
    triangle = a + c > c and b + c > a and a + c > b
    print(f"Puede formar un triángulo: {triangle}")
