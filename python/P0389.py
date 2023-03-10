#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

import collections


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.defaultdict(int)

        for ch in s:
            dic[ch] += 1

        for ch in t:
            if ch not in dic:
                return ch

            dic[ch] -= 1

        for ch, nums in dic.items():
            if nums < 0:
                return ch

        return ""