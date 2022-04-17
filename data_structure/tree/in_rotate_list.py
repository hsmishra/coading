"""
Search an element in a sorted and rotated array (logN) 
"""


def search_element(lst, left, right, ele):
    if right >= left:
        mid = left + (right-left) // 2

        if lst[mid] == ele:
            return mid

        # If left to mid is sorted then ...
        if lst[left] <= lst[mid]:
            if ele >= lst[left] and ele <= lst[mid]:
                return search_element(lst, left, mid-1, ele)
            return search_element(lst, mid+1, right, ele)
        
        # If left to mid is not sorted, then mid to right mush be sorted 
        if ele >= lst[mid] and ele <= lst[right]:
            return search_element(lst, mid+1, right, ele)
        return search_element(lst, left, mid-1, ele)

    return -1

if __name__ == "__main__":

    lst = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    left = 0
    right = len(lst)-1
    ele = 21
    print(search_element(lst, left, right, ele))