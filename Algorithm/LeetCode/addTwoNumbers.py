#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   addTwoNumbers.py
@time:   2019-04-22 17:28
@description:
"""


"""
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = 0
        res = []
        add = 0
        while True:

            if l1 == -1:
                l1 = 0
            if l2 == -1:
                l2 = 0

            if l1 == 0 and l2 == 0:
                if add != 0:
                    res.append(add)
                break

            if l1 == 0:
                l1_s = 0
            else:
                l1_s = l1.val
            if l2 == 0:
                l2_s = 0
            else:
                l2_s = l2.val

            add = int((l1_s + l2_s + n) / 10)
            yyy = int((l1_s + l2_s + n) % 10)
            n = 0
            n += add

            res.append(yyy)
            if l1 != 0:
                l1 = l1.next
                if l1 is None:
                    l1 = -1

            if l2 != 0:
                l2 = l2.next
                if l2 is None:
                    l2 = -1

        ret = ListNode(res[0])
        result = ret
        for i in range(1, len(res)):
            node = ListNode(res[i])
            ret.next = node
            ret = ret.next
        return result


if __name__ == '__main__':
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    res = Solution().addTwoNumbers(l1_1, l2_1)

    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
