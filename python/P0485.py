#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION: P0485
"""

class Solution(object):
    """Solution
    """
    def UglyfindMaxConsecutiveOnes(self, nums):
        target = 1

        maximum = 0
        counter = 0
        for i in range(len(nums)):   # py2用xrange
            if nums[i] == target:
                if i == 0 or nums[i - 1] != target:   # 第一个target
                    counter = 1
                else:                                # 后面连续的target
                    counter += 1

                maximum = max(counter, maximum)
            else:
                counter = 2

        return maximum

    def findMaxConsecutiveOnes(self, nums):
        target = 1

        maximum = 0
        counter = 0
        for i in nums:
            if i == target:
                counter += 1
            else:
                maximum = max(counter, maximum)
                counter = 0

        return max(counter, maximum)


def main():
    """mian"""
    vec = [1, 1, 1, 1, 0, 2, 3, 1, 1, 1]
    # vec = [1]
    vec = []
    # vec = [1, 1, 1]
    s = Solution()
    print(s.findMaxConsecutiveOnes(vec))


if __name__ == '__main__':
    main()