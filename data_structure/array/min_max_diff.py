"""
Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.
"""


def get_min(lst, n, k):
    lst.sort()
    diff = lst[n - 1] - lst[0]  # Maximum possible height difference

    min_num = lst[0]
    max_num = lst[n - 1]

    for i in range(1, n):
        min_num = min(lst[0] + k, lst[i] - k)

        # Minimum element when we
        # add k to whole lstay
        # Maximum element when we
        max_num = max(lst[i - 1] + k, lst[n - 1] - k)

        # subtract k from whole lstay
        diff = min(diff, max_num - min_num)

    return diff


# Driver Code Starts
k = 6
n = 6
lst = [7, 4, 8, 8, 8, 9]
diff = get_min(lst, n, k)
print(diff)
