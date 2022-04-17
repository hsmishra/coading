"""
Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
"""


def double_of_given_no(num):
    return lambda x: x*num


def triple_of_given_no(num):
    return lambda x: x*num


res_double = double_of_given_no(12)
res_triple = triple_of_given_no(12)

print(res_double(2))
print(res_triple(3))
