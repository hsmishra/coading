from array import array


def search_postion(lst, left, right, ele):
    if right >= left:
        mid = left + (right - left) // 2
        if ele == lst[mid]:
            return mid
        elif ele > lst[mid]:
            return search_postion(lst, mid+1, right, ele)
        else:
            return search_postion(lst, left, mid-1, ele)
    return -1


def count_pairs(lst, num, k):
    counter = 0
    lst.sort()
    for i in range(0, num-2):
        if (search_postion(lst, i + 1, num - 1, lst[i] + k) != -1):
            counter += 1
    return counter


lst = [1, 5, 3, 4, 2]

num = len(lst)

k = 4

print(count_pairs(lst, num, k))


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

def find_pair(lst, diff):

    # sort list in ascending order
    lst.sort()

    # take an empty set
    s = set()

    # do for every element in the list
    i = 0
    while i < len(lst):

        # to avoid printing duplicates (skip adjacent duplicates)
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            i = i + 1

        # check if pair with the given difference `(lst[i], lst[i]-diff)` exists
        if lst[i] - diff in s:
            print((lst[i], lst[i] - diff))

        # check if pair with the given difference `(lst[i]+diff, lst[i])` exists
        if lst[i] + diff in s:
            print((lst[i] + diff, lst[i]))

        # insert the current element into the set
        s.add(lst[i])

        i = i + 1


if __name__ == '__main__':

    lst = [1, 5, 3, 4, 2]
    diff = 4

    find_pair(lst, diff)
