def posicion_insercion(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Complejidad: O(log n) tiempo, O(1) espacio

# estudiar esta idea:
# def otra_solucion(m, t, l, r):
#     if l == r:
#         return M[l//2][l%2] == t
#     mi = (l+r) // 2
#     if t <= M[l//m][l%m]:

#vacas agresivas
def vacas_agresivas(vacas): #idea: hacer busqueda binaria sobre la distanncia
    # funciin qye ponga una vaca en el establo y compare las distancias, si esta a una distancia menor igual mueve la vaca
    left,right = 0, len(vacas) - 1
    while left <= right:
        pass

#busqueda lineal vs busqueda binaria
#bus1ueda binaria: es util hacerla sobre la respuesta
def cp13(matriz):
    lista_plana = []
    for i in matriz:
        for j in i:
            lista_plana.append(j)
    return lista_plana

# ejercicio: buscar en una matriz(lista de listas) un numero

print(cp13([[1, 2, 3],[4, 5, 6]]))

# print(posicion_insercion(nums = [1, 3, 5, 6], target = 4))