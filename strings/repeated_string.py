"""
Given an integer N and a lowercase string. The string is repeated infinitely.
The task is to find the No. of occurrences of a given character x in first N letters.


Input : N = 10 str = "abcac"
Output : 4
Explanation: "abcacabcac" is the substring from the infinitely repeated string. In first 10 letters 'a' occurs 4  times.

Input: N = 10, str = "aba"
Output : 7
"""


def countChar(str, x):
    count = 0
    for i in range(len(str)):
        if (str[i] == x):
            count += 1
    n = 4

    repititions = n // len(str)
    count = count * repititions

    l = n % len(str)
    for i in range(l):
        if (str[i] == x):
            count += 1
    return count


# Uncomment the below line number 31 and 32 for calling above function

# str = "satyam"
# print(countChar(str, 'a'))

# Using single line -----------------

name = "abcacabcac"
num = 10

res = name.count("a") * (num//len(name)) + name[num % len(name)].count('a')

print(res)
