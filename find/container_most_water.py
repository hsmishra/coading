"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

LeetCode: https://leetcode.com/problems/container-with-most-water/
"""


def max_water(height):
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


# Driver code
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(max_water(a))
