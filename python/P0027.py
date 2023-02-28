#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

class Solution(object):
    """Solution"""
    def Old_removeElement(self, nums, val):
        """v1版本，后面有个index记录[垃圾箱]的下标"""
        # high 为从后往前，第一个 != val 的index
        high = len(nums) - 1
        while high >= 0 and nums[high] == val:
            high -= 1

        low = 0
        while low <= high:
            if nums[low] == val:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
            else:
                low += 1

        return high + 1

    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i


def main():
    """main"""
    s = Solution()

    # vec, val = [3, 2, 2, 3], 2
    vec, val = [], 0
    vec, val = [1, 1, 1, 1], 1
    vec, val = [0, 1, 2, 2, 3, 0, 4, 2], 3

    print(s.removeElement(vec, val), vec)


if __name__ == '__main__':
    main()