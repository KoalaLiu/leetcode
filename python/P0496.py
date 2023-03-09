#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res_dict = dict()
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:   # 当前元素大于栈顶
                key = stack.pop()
                res_dict[key] = num

            stack.append(num)

        res = []
        for num in nums1:
            res.append(res_dict.get(num, -1))

        return res
