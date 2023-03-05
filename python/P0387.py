#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        stat = collections.defaultdict(int)
        for ch in s:
            stat[ch] += 1

        for i, ch in enumerate(s):
            if stat[ch] == 1:
                return i
        return -1
