from bisect import bisect_left, bisect_right


def search(nums, target):
    if not nums:
        return [-1, -1]
    n = len(nums)
    st, end = -1, -1
    left = bisect_left(nums, target)
    right = bisect_right(nums, target)
    if left < n and nums[left] == target:
        st = left
    if nums[right-1] == target:
        end = right-1
    return [st, end]


lst = [1, 2, 2, 3, 4, 6, 6]

print(search(lst, 4))
