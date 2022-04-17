"""
There is another implementation of this using stack please look,
in stack folder
"""

def rightmost_greater(arr, left, right):
    if left <= right:
        if arr[left]  > arr[right]:
             rightmost_greater(arr, left, right-1)
        else:
            lst.append(arr[right])
            rightmost_greater(arr, left+1, n-1)

    return lst


arr = [16, 17, 4, 3, 5, 2]
lst = []
n = len(arr)
print(rightmost_greater(arr, 0, n-1))





