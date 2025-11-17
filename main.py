# import sys

# while True:
#     print("Menú de Navegación:")
#     print("1. Ejecutar cp01")
#     print("2. Ejecutar cp02")
#     print("3. Ejecutar cp03")
#     print("4. Ejecutar cp04")
#     print("5. Ejecutar cp05")
#     print("6. Salir")
#     choice = input("Elige una opción: ")
#     if choice == '1':
#         import cps.cp01 as cp01
#         cp01.di_hola()
#         cp01.recibiendo_entradas()
#         cp01.hanoi_towers()
#         cp01.max_min()
#     elif choice == '2':
#         import cps.cp02 as cp02
#         cp02.formando_fechas()
#         cp02.calculate_final_amount()
#         cp02.discount()
#         cp02.atm()
#         cp02.triangle_type()
#         cp02.right_order()
#     elif choice == '3':
#         import cps.cp03
#     elif choice == '4':
#         import cps.cp04
#     elif choice == '5':
#         import cps.cp05
#     elif choice == '6':
#         sys.exit()
#     else:
#         print("Opción inválida")
