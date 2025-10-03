def formando_fechas():
    day = int(input("Introduce the day "))
    month = int(input("Introduce the month "))
    year = int(input("Introduce the year "))

    if day <= 0 or (0 >= month > 12) or year <= 0: #the same as in line 96 with the inequalities
        print("valores inválidos")
    elif (4 < day < 15) and month == 10 and year == 1582: #(4 < day < 15) better than (day > 4 and day < 15)
        print("fecha inválida")

    if month%2 == 0:
        print()

def calculate_final_amount():
    try:
        purchase_amount = float(input("Ingrese el monto de la compra: ").strip())
        is_vip = input("¿Es usted miembro VIP? (si/no): ").strip().lower()

        if purchase_amount > 1000 or is_vip == "si":
            discount = purchase_amount * 0.15
            final_amount = purchase_amount - discount
        else:
            final_amount = purchase_amount

        print(f"El monto final a pagar es: ${final_amount:.2f}")

    except ValueError:
        print("Error: Por favor, ingrese un monto de compra válido.") #i should put it into a loop to ask for the input until the entry is valid 


def discount():
    total_due = int(input("How much is the total? "))
    vip = input("Are you vip, yes or not? ")

    if vip == "yes" or total_due > 1000:
        print("Total due is", total_due * 0.85)
    else:
        print("Total due is", total_due)

def atm():
    balance = int(input("What is your current balance? "))
    withdrawal_amount = int(input("Enter the amount to withdraw "))
    error = False

    if withdrawal_amount <= 0:
        error = True
        print("Withdrawal amount cannot be negative or 0")
    if balance < withdrawal_amount:
        error = True
        print("Insufficient balance")
    if withdrawal_amount%10 != 0:
        error = True
        print("Withdrawal amount must be a multiple of 10")
    if error == False:
        print("Remaining balance:", balance - withdrawal_amount)

def triangle_type():
    a = int(input("enter side a "))
    b = int(input("enter side b "))
    c = int(input("enter side c "))
    right_angled = False
    #abs(a + b) >= abs(a) + abs(b) and abs(b + c) >= abs(b) + abs(c) and abs(a) + c >= abs(c) + abs(c)
    if abs(a + b) < c and abs(b + c) < a and abs(a + c) < b:
        print("this is not a valid triangle")
    else:
        if (a**2) + (b**2) == (c**2) or (b**2) + (c**2) == (a**2) or (a**2) + (c**2) == (b**2):
            right_angled = True
        if a == b and b == c: #by transitivity a == c
            print(f"the triangle is equilateral and isosceles")
        if a != b and b != c and a != c:
            print(f"the triangle is scalene {"and a right triangle" if right_angled else " "}")
        if a == b and b != c or b == c and c != a or a == c and a != b:
            print(f"the triangle is isosceles {"and a right triangle" if right_angled else " "}")

def right_order():
    num1 = int(input("introduce the first number "))
    num2 = int(input("introduce the second number "))
    num3 = int(input("introduce the third number "))

def intervals():

def the_day_after():

def a_triangle_and_a_point():