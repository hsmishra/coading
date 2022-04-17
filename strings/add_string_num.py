"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"
"""


def addStrings(num1: str, num2: str) -> str:
    result = ""
    carry = 0

    def equalize_charecters(num1, num2):
        if len(num1) < len(num2):
            while len(num1) != len(num2):
                num1 = "0" + num1
        else:
            while len(num2) != len(num1):
                num2 = "0" + num2
        return [num1, num2]

    num1, num2 = equalize_charecters(num1, num2)
    lst1, lst2 = list(num1), list(num2)
    while len(lst1) != 0:
        add = int(lst1.pop()) + int(lst2.pop()) + int(carry)
        carry = add // 10
        result = str(add % 10) + result
        if carry != 0:
            result = str(carry) + result
    return result


num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
