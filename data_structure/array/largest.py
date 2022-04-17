def find_largest(num):
    large = num.index(max(num))
    small = num.index(min(num))
    return f"Max is {large} and Small is {small}"


lst =  [4, 1, 6, 9, 10, 7, 0]
print(find_largest(lst))




# lst = [4, 1, 6, 9, 10, 7, 0]


# max_index = max((item, index) for index, item in enumerate(lst))[1]

# min_index = min((item, index) for index, item in enumerate(lst))[1]

# print(f"max_index is {max_index}")
# print(f"min_index  is {min_index}")
