#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""


class Solution(object):
    def On2maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return 0

        res = []

        i, j = 0, k
        while j <= len(nums):
            window = nums[i:j]

            res.append(max(window))

            i += 1
            j += 1

        return res
 
    def maxSlidingWindow(self, nums, k):
        # win保留index，并且保证 从大到小 排列
        win, res = [], []

        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:  # win顶不在窗口范围内，直接pop(0)
                win.pop(0)

            while win and nums[win[-1]] < v:  # 队底比v小，直接pop掉
                win.pop()

            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])

        return res


def main():
    """main"""
    s = Solution()

    vec, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    # vec, k = [1, 2, 3], 3
    # vec, k = [], 0

    print(s.maxSlidingWindow(vec, k))


if __name__ == "__main__":
    main()
