def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[j] <= numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers


# Solucion 1 con set built-in functions
def merge_timelines(timelines):
    timelines_list = []
    for i in timelines:
        for j in i:
            timelines_list.append(j)

    sorted_list = selection_sort(list(set(timelines_list)))
    
    return sorted_list


# Solucion 2 sin set built-in function
def merge_timelines2(timelines):
    timelines_list = []
    for i in timelines:
        for j in i:
            timelines_list.append(j)

    dedupled_list = []
    for timeline in timelines_list:
        if timeline not in dedupled_list:
            dedupled_list.append(timeline)

    sorted_list = selection_sort(dedupled_list)

    return sorted_list

def reagrupar_listas(valores, indices_pertenencia):
    # los indices de pertencecia son los indices de una lista de listas
    output = []
    max_idx = max(indices_pertenencia)
    for i in range(max_idx):
        lista = []
    for i in 

    return output




reagrupar_listas(valores=[1, 2, 3], indices_pertenencia=[1, 2, 1])