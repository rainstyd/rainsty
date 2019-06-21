#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   longestPalindrome.py
@time:   2019-05-29 11:59
@description:
"""

"""
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    
    Example 2:
    Input: "cbbd"
    Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        if len(list(set(s))) == 1:
            return s
        if len(list(set(s))) == len(s):
            return s[0]

        s_len = len(s)

        length = 0
        max_length = 0
        position = 0
        max_position = 0
        middle = 0
        max_middle = 0
        result = list()

        for r in range(s_len):
            print(result, max_position, max_length, max_middle)
            if s[r] not in result:
                if middle == 0:
                    result.append(s[r])
                    length += 1
                else:
                    result = result[middle:]
                    result.append(s[r])
                    length = len(result)
            else:
                if s[r] == s[r - 1]:
                    max_length_1 = 2
                    if max_length < max_length_1:
                        max_length = max_length_1
                        max_position = r - 1
                        max_middle = middle
                    result.append(s[r])
                    result = result[-1:]
                    length = len(result)
                else:
                    if middle == 0:
                        middle = length - 1
                    if s[r] == s[r - 2]:
                        middle = length - 1
                        result.append(s[r])
                        length += 1
                        if max_length < length:
                            max_position = r - length + 1
                            max_length = length
                            max_middle = middle
                    else:
                        if (middle - result.index(s[r])) == (length - middle):
                            result.append(s[r])
                            length += 1
                            if length > max_length:
                                max_length = length - result.index(s[r])
                                position = r - length + 1
                                max_middle = middle

                        else:
                            result = result[(middle - result.index(s[r]) + 1):]
                            middle = 0
                            result.append(s[r])
                            length = len(result)

        print(result, max_position, max_length, max_middle)

        result = s[max_position:max_length + max_position]

        r = max_length - max_middle
        print(r)
        result = result[r:max_middle+r]

        if result == '':
            result = s[0]

        return result


if __name__ == '__main__':
    _s = "eabcb"
    _lp = Solution().longestPalindrome(_s)
    print(_lp)
