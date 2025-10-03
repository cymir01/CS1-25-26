# listas y tuplas (estructuras de datos ordenadas)
# conceptos: mutabilidad y referencia

#CACHARREO CON EL CONTENIDO DE LA CONFERENCIA 03
notas = ["cynthia", "marco", 100, True, [2, 3, 4], [], "pepe"]
position = 1
print("El nombre es", notas[position])
print("elementos de la lista:", len(notas))
print(notas[len(notas) - 1])
print(notas[-1])
if "cynthia" in notas:
    del notas[-1]
    print(notas)
print(notas[-3:])
print(notas[2:4])

#hallar términos del medio sin conocer el tamaño de la lista
# la división entera garantiza que no haya floats como índices, cosa que daría error, por ejemplom para el caso lista = [3]
lista = [3] 
cardinalidad = len(lista)
if cardinalidad == 0:
    print([])
if cardinalidad%2 == 0:
    print(lista[(cardinalidad // 2) - 1], lista[cardinalidad // 2])
else:
    print(lista[cardinalidad // 2])

k = 2
lista = [4, 6, 7, 8, 0]
menores = []
for x in lista:
    if x < k:
        menores.append(x)
print(menores)
