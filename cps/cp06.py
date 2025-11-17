# def hi(name):
#     print("Hi", name)

# hi(input("nombre\n"))
# def spam(): 
#     eggs = 31337
#     return eggs
# print(spam())

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers
# TODO: HACER UNA EXCEPCION PARA EL CASO EN QUE SE REPITA EL MISMO NUMERO


def quicksort():
    pass


def mergesort():
    pass
# print(selection_sort([4, 2, 1]))


def sort_with_key():
    tuples = [(1, 30), (2, 20), (3, 90), (4, 10), (5, 90)]
    values = []
    for tuple in tuples:
        for i in range(len(tuple)):
            if i == 1:
                values.append(tuple[i])
                sorted_values = selection_sort(values)

    print(sorted_values)


# sort_with_key()
