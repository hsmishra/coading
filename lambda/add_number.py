"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""

add_number = lambda x:x+15
multiplies = lambda x, y:x*y

print(add_number(5))
print(multiplies(20, 5))