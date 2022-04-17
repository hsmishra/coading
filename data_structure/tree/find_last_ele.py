def find_last_index(lst, start, end, ele, num):
    if (end >= start):
        mid = start + (end - start) // 2
        if ((mid == num - 1 or ele < lst[mid + 1]) and lst[mid] == ele):
            return mid
        elif (ele < lst[mid]):
            return find_last_index(lst, start, (mid - 1), ele, num)
        else:
            return find_last_index(lst, (mid + 1), end, ele, num)

    return -1


lst = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
num = len(lst)

ele = 2
print("find_last_index Occurrence = ",
      find_last_index(lst, 0, num - 1, ele, num))
