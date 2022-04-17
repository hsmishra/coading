# Python program to find largest, smallest,
# second largest and second smallest in a
# list with complexity O(n)
def find_num(lst):
    largest = lst[0]
    lowest = lst[0]
    second_largest = None
    second_lowest = None
    for item in lst[1:]:
        if item > largest:
            second_largest = largest
            largest = item
        elif second_largest == None or second_largest < item:
            second_largest = item
        if item < lowest:
            second_lowest = lowest
            lowest = item
        elif second_lowest == None or second_lowest > item:
            second_lowest = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", second_largest)
    print("Second Smallest element is:", second_lowest)


# Driver Code
lst = [12, 45, 2, 41, 31, 10, 8, 6, 4]
find_num(lst)
