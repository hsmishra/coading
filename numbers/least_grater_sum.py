"""
Least Greater number with same digit sum
---> We divide the number into 4 regions :
---> 1st: Trailing zeros.
---> 2nd: The lowest digit not in Region 1.
---> 3rd: Consecutive 9s starting with the digit above Region 2.
---> 4th: All remaining digits.

Then the next number is :
[Region 4+1] [Region 1] [Region 2-1] [Region 3] .

Example:
Input Number = 548995000
Region 1 : 000
Region 2 : 5
Region 3 : 99
Region 4 : 548

Next number = 549000499 
"""
# Python3 program to find next greater number with
# same sum of digits.


def next_gratest(lst, num):

    # for storing 4 regions
    trailings = []
    decrements = []
    midNines = []
    rem = []

    # trailing zeros region1
    i = num - 1  # last index
    while (lst[i] == 0):
        trailings.append(0)
        i -= 1

    # lowest region(region 2) not in region 1
    decrements.append(lst[i])
    i -= 1

    # Consecutive 9's (region 3)
    while (lst[i] == 9):
        midNines.append(9)
        i -= 1

    j = 0
    while (lst[j] == 0):
        j += 1  # Starting zeros

    while (j <= i):  # 4th region
        rem.append(lst[j])
        j += 1

    # Calculation of result
    j = len(rem) - 1

    rem[j] += 1  # Region4 + 1

    decrements[0] -= 1  # Region2 -1

    l = len(trailings) + len(decrements) + len(midNines) + len(rem)

    # Calculating the result
    j = num-1
    i = len(midNines) - 1

    # Copying the third region
    while (i >= 0):
        lst[j] = midNines[i]
        j -= 1
        i -= 1

    # Copying the 2nd region
    i = len(decrements) - 1
    while (i >= 0):
        lst[j] = decrements[i]
        j -= 1
        i -= 1

    # Copying the 1st region
    i = len(trailings) - 1
    while (i >= 0):
        lst[j] = trailings[i]
        j -= 1
        i -= 1

    # Copying the 4th region
    i = len(rem) - 1
    while (i >= 0):
        lst[j] = rem[i]
        j -= 1
        i -= 1

    while (j >= 0):
        lst[j] = 0
        j -= 1


# Driver code
lst = [1, 9, 9, 0]
num = len(lst)

next_gratest(lst, num)  # Calling the function

for i in range(0, num):
    print(lst[i], end="")
