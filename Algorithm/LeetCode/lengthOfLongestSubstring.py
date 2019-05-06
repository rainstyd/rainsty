#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   lengthOfLongestSubstring.py
@time:   2019-05-06 09:07
@description:
"""

"""
    Given a string, find the length of the longest substring without repeating characters.
    
    Example 1:
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    
    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
                return 1
        a = 0
        e = []
        for r in range(len(s)):
            if s[r] in e:
                e = e[e.index(s[r])+1:]
                e.append(s[r])
            else:
                e.append(s[r])
            if a < len(e):
                    a = len(e)
            # print(e)
        return a


if __name__ == '__main__':
    s = 'abcdaafdaf'
    r = Solution().lengthOfLongestSubstring(s)
    print(r)
