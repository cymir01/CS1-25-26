# listas y tuplas (estructuras de datos ordenadas)
# conceptos: mutabilidad y referencia

#CACHARREO CON EL CONTENIDO DE LA CONFERENCIA 03
def cacharreo_c03():
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
# la división entera garantiza que no haya floats como índices, cosa que daría error, por ejemplo para el caso lista = [3]
def terminos_medios():
    lista = [3] 
    cardinalidad = len(lista)
    if cardinalidad == 0:
        print([])
    if cardinalidad%2 == 0:
        print(lista[(cardinalidad // 2) - 1], lista[cardinalidad // 2])
    else:
        print(lista[cardinalidad // 2])

def filtrado_pro():
    k = int(input("entero k\n"))
    # with list comprehension
    entrada = input("Ingrese los enteros de la lista separados por espacio\n")
    lista = [int(x) for x in entrada.split()]
    menores = []
    for i in lista:
        if i < k:
            menores.append(i)
    return menores

def filtrado_pro_plus():
    A = ["Ana", "Ben", "Alonso"]
    B = ["Ben", "Guillermo", "Ana", "Ramon"]
    index_list = []

    for i in B:
        if i in A:
            indice = 2A.index(i)
            index_list.append(indice)
        else:
            index_list.append(-1)
    print(index_list)

def LShift_Pro():
    A = [2, 3, 4]
    new_list = []

    for x in A:

        
    new_list.append()


    print(new_list)






