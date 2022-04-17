# Function to find sublists with the given sum in a list
def findSublists(nums, target):
    for i in range(len(nums)):
        sums = 0
        for j in range(i, len(nums)):
            sums += nums[j]
            if sums == target:
                print(nums[i:j+1])


if __name__ == '__main__':

    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    target = 7

    findSublists(nums, target)


# ===========================


# Function to find sublists with the given sum in a list
def find_subarray(nums, target):
    d = {}

    # To handle the case when the sublist with the given sum starts
    # from the 0th index
    d.setdefault(0, []).append(-1)

    sums = 0

    # traverse the given list
    for index in range(len(nums)):

        # target of elements so far
        sums += nums[index]

        # check if there exists at least one sublist with the given sum
        if (sums - target) in d:
            print(*[nums[value+1: index+1]
                  for value in d.get(sums-target)], end=' ')

        # insert (target so far, current index) pair into the dictionary
        d.setdefault(sums, []).append(index)


if __name__ == '__main__':

    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    target = 7

    find_subarray(nums, target)
