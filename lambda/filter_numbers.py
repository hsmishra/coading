"""
Write a Python program to filter a list of integers using Lambda.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers
print(list(filter(lambda x: x % 2 == 0, nums)))

# Odd number
print(list(filter(lambda x: x % 2 != 0, nums)))
