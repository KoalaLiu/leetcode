#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION: P0283
"""

class Solution(object):
    """Solution"""

    def Old_moveZeroes(self, nums):
        # 冒泡的方式
        num_non_zeroes = len(nums)
        idx = 0
        while idx < num_non_zeroes:
            if nums[idx] == 0:
                num_non_zeroes -= 1
                for j in range(idx, len(nums) - 1):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                idx += 1

        return nums

    def moveZeroes(self, nums):
        # 一次遍历的方式
        i = 0  # 非0数字的index
        for j, num in enumerate(nums):
            if num != 0:
                nums[i] = num

                if i < j:   # 如果j>i，则j位置的数字用完了，就可以赋值为0了
                    nums[j] = 0
                i += 1

        return nums


def main():
    """main"""
    s = Solution()

    vec = [0, 1, 0, 3, 12]
    # vec = [0]
    # vec = [1, 2, 3, 0, 0]
    # vec = [0, 0, 0]
    # vec = [0, 0, 1]

    print(s.moveZeroes(vec))


if __name__ == "__main__":
    main()