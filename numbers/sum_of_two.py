def twoSum(nums, target):
    dictionary = {}

    for i in range(len(nums)):
        secondNumber = target-nums[i]
        if(secondNumber in dictionary.keys()):
            secondIndex = nums.index(secondNumber)
            if(i != secondIndex):
                return sorted([i, secondIndex])

        dictionary.update({nums[i]: i})


lst = [2, 1, 4, 3, 9, 6, 8, 7, 5]

target = 9

print(twoSum(lst, target))
