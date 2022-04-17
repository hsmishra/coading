"""
Given an array of positive and negative numbers,
arrange them in an alternate fashion such that every
positive number is followed by negative and vice-versa
maintaining the order of appearance.
"""

def find_first_positive(lst):
    j = 0
    pivot = 0

    for i in range(len(lst)):
        if lst[i] < pivot:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            j = j+1

    return j # it is holding first index of positive number


# now let's arrange the list such that it contains 1 +ve and 1 -ve
def re_arrange_numbers(lst):
    p = find_first_positive(lst)

    num = 0

    while len(lst) > p >num:
        temp = lst[num]
        lst[num] = lst[p]
        lst[p] = temp

        p += 1
        num += 2

lst = [9, -3, 5, -2, -8, -6, 1, 3, 1, 12, 43, 56]

re_arrange_numbers(lst)

print(lst)

