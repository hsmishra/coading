"""
Given a sorted array with possibly duplicate elements, 
the task is to find indexes of first element x in the given arra
"""

def find_first_index(lst, start, end, ele, num):

    mid = start + (end - start) // 2
    if(end >= start):
        if((mid == 0 or ele > lst[mid - 1]) and lst[mid] == ele):
            return mid
        elif(ele > lst[mid]):
            return find_first_index(lst, (mid + 1), end, ele, num)
        else:
            return find_first_index(lst, start, (mid - 1), ele, num)

    return -1


# Driver program
lst = [1, 2, 2, 4, 4, 5, 6, 7, 7, 7, 7, 8]
num = len(lst)

ele = 4
print(find_first_index(lst, 0, num - 1, ele, num))
