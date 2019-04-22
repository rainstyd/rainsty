#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   twoSum.py
@time:   2019-04-22 13:43
@description:
"""

from datetime import datetime

"""
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


class Solution01(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in range(len(nums) - 1):
            for u in range(n, len(nums) - 1):
                if nums[n] + nums[u + 1] == target:
                    return [n, u + 1]


class Solution02(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in range(len(nums)):
            if target - nums[n] in nums:
                for u in range(n+1, len(nums)):
                    if nums[u] == target - nums[n]:
                        return [n, u]


if __name__ == '__main__':
    start = datetime.now()
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution02()
    twoSum = solution.twoSum(nums, target)
    print(twoSum)
    print(datetime.now() - start)
