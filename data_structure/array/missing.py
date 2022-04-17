def find_missing(array):
    return [x for x in range(array[0], array[-1]) if x not in array]


lst = [2, 4, 1, 7, 10]

print(find_missing(lst))
