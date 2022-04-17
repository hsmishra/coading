lst = [0, 2, 3, 5, 6, 7, 9, 10]
missing_elements = []
for ele in range(lst[0], lst[-1]+1):
    if ele not in lst:
        missing_elements.append(ele)
print(missing_elements)

# ========================================== List Comprehension ========================
lst = [1, 2, 3, 4, 5, 7, 6, 9, 10]
missing_numbers = [item for item in range(
    lst[0], lst[-1]+1) if item not in lst]
print(missing_numbers)

# ========================================== Set  ========================

lst = [1, 2, 3, 4, 5, 7, 6, 9, 10]
missing_numbers = set(range(lst[0], lst[-1]+1)) - set(lst)
print(missing_numbers)

# ========================================== XoR  ========================


def get_missing_number(lst):

    # Compute XOR of all the elements in the list
    xor = 0
    for i in lst:
        xor = xor ^ i

    # Compute XOR of all the elements from 1 to `n+1`
    for i in range(1, len(lst) + 2):
        xor = xor ^ i

    return xor


if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print('The missing number is', get_missing_number(lst))
