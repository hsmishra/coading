"""
Given an array of integers. Find a peak element in it. An array element is a peak if it is NOT smaller than its neighbours. For corner elements, we need to consider only one neighbour. 

Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbours 23 and 67.

"""


def get_peak(lst, n):

    # first or last element is peak element
    if (n == 1):
        return 0
    if (n == 2):
        if (lst[0] >= lst[1]):
            return 0
    if (lst[n - 1] >= lst[n - 2]):
        return n - 1

    for i in range(1, n - 1):

        if (lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]):
            return i


# # Driver code.
arr = [1, 0, 0, 0, 3, 90]
n = len(arr)
print("Index of a peak point is", get_peak(arr, n))

# =================================================================================================


def get_peak(lst):
    n = len(lst)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if(mid == 0 or lst[mid-1] <= lst[mid]) and (mid == n-1 or lst[mid] >= lst[mid+1]):
            return mid
        if mid == 0 or lst[mid-1] > lst[mid]:
            right = mid-1
        else:
            left = mid+1


lst = [1, 2, 1, 3, 5, 6, 4]
print("==============")
print(get_peak(lst))
