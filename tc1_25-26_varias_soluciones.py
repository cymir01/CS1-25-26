def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[j] <= numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers

def selection_sort_with_set_list_function(numbers):
    numbers_list = list(numbers)
    for i in range(len(numbers_list) - 1):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[j] < numbers_list[i]:
                numbers_list[j], numbers_list[i] = numbers_list[i], numbers_list[j]
    return numbers_list

def selection_sort_with_set_for_loop(numbers):
    numbers_list = []
    for i in numbers:
        numbers_list.append(i)

    for i in range(len(numbers_list) - 1):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[j] < numbers_list[i]:
                numbers_list[j], numbers_list[i] = numbers_list[i], numbers_list[j]
    return numbers_list

selection_sort_with_set_for_loop({3, 2, 1, 0})

# Solucion 1 con list y set built-in functions
def merge_timelines(timelines):
    timelines_list = []
    for i in timelines:
        for j in i:
            timelines_list.append(j)

    sorted_list = selection_sort(list(set(timelines_list)))
    
    return sorted_list


# Solucion 2 sin list y set built-in functions
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

# print(merge_timelines2([[45.2, 3, 9], [2, 6], [3, 4, 7]]))

