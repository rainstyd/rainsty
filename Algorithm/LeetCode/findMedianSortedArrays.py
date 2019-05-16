#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   findMedianSortedArrays.py
@time:   2019-05-16 18:04
@description:
"""

"""
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.
    
    Example 1:
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0
    
    Example 2:
    
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if len(nums) % 2 == 1:
            return nums[int(l / 2)]
        else:
            return float(nums[int(l / 2)] + nums[int(l / 2 -1)]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    res = Solution().findMedianSortedArrays(nums1, nums2)
    print(res)
