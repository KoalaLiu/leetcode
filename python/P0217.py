#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stat = {}
        for num in nums:
            if num in stat:
                return True

            stat[num] = 1

        return False
