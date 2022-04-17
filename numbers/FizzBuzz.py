"""
using list comprehention wite a FizzBuzz program 
"""

res = ["Fizz"*(not i % 3)+"Buzz"*(not i % 5) or i for i in range(0, 100)]

print(res)