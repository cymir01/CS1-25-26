from rich.console import Console
blue_console = Console(style="white on blue")

# # li = ["geeks", "for", "geeks"]
# # for x in range(len(li)):
# # 	print(li[x])
# # while True: 
# # 	print('Please type your name.')
# # 	name = input()
# # 	if name == 'Cynthia': 
# # 		break
# # print('Thank you!')

# # while True: 
# # 	print('Who are you?') 
# # 	name = input()
# # 	if name != 'Joe':
# # 		continue 
# # 	print('Hello, Joe. What is the password? (It is a fish.)')
# # 	password = input()
# # 	if password == 'swordfish':
# # 		break
# # print('Access granted.')

# # print('My name is') 
# # for i in range(5): 
# # 	print('Jimmy Five Times (' + str(i) + ')')

# # print('My name is') 
# # i=0 
# # print(str(0))
# # while i < 5: 
# # 	print('Jimmy Five Times (' + str(i) + ')')
# # 	i += 1

# # valores = [2, 3]
# # sumatoria = 0

# # for i in valores:
# # 	sumatoria += i
# # print(sumatoria)

# # def busqueda_secuencial(catalogo, buscado):
# # 	encontrado = False
# # 	for producto in catalogo:
# # 		if producto == buscado:
# # 			encontrado = True
# # 	if encontrado:
# # 		return 'esta'
# # 	else:
# # 		return 'no esta'

# # print(busqueda_secuencial([4, 5], 5))

# def averiguaciones():
#     requested_data = ["age", "height", "location"]
#     testimonials = [
#         {"age": 20},
#         {"height": 1.7},
#         {"location": 'Park Avenue'}
#     ]
    
#     # Para verificar si tenemos toda la información
#     datos_encontrados = set()
    
#     # Para detectar contradicciones
#     valores_por_dato = {}
    
#     # Recorrer cada dato que necesitamos
#     for dato in requested_data:
#         # Recorrer cada testimonio
#         for testimonial in testimonials:
#             # Recorrer cada clave-valor del testimonio
#             for clave, valor in testimonial.items():
#                 if dato == clave:
#                     print(f'Encontrado: {clave} = {valor}')
#                     datos_encontrados.add(dato)
                    
#                     # Guardar valores para detectar contradicciones
#                     if dato not in valores_por_dato:
#                         valores_por_dato[dato] = set()
#                     valores_por_dato[dato].add(valor)
    
#     # 1. Verificar si tenemos toda la información
#     informe_completo = len(datos_encontrados) == len(requested_data)
    
#     # 2. Encontrar datos contradictorios
#     datos_contradictorios = []
#     for dato, valores in valores_por_dato.items():
#         if len(valores) > 1:
#             datos_contradictorios.append(dato)
    
#     return informe_completo, datos_contradictorios

# # Llamar a la función
# resultado = averiguaciones()
# print(f"Resultado: {resultado}")

#-----------ESTUDIAR ESTE CODIGO Y ENTENDER POR QUE NO WORK BREAK--------
# n = int(input('numero?'))
# i = 2
# while i < n:
#     if n % i == 0:
#         print(f'{n} no es primo')
#         break
#     else:
#         print(f'{n} es primo')
#---------------------------------------------

# l = [1] * 10
# l[5] = 2
# for i in range(len(l)):
#     if l[i] != 1:
#         print(f'posicion: {i}')
# print("termino")

# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)

# # myfunc()

# print("Python is " + x)
