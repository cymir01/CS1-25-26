# a = [7, 2, 3]
# b = [4, 6, 8]
# for i in b:
#     for j in a:
#         if (i%j == 0):
#             print(i)
#             break

# #hacer una matriz

# k = 5
# i = 0
# l = [1, 2, 3, 5]
# while i < len(l):
#     if l[i] == k:
#         print(f"El valor {k} esta en la posicion {i}")
#         break
#     i += 1
# else:
#     print(f"El valor {k} no esta en la lista")

# words = [1, 2, 3]
# for i in words:
#     print(i, len(i))

#TODO: ver como leer listas de la consola y guardarlas
A = [4, 5, 6]
B = [4, 12, 1]
for i in B:
    for j in A:
        if i%j == 0:
            print(i)
            break
