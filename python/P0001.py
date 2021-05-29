class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = dict()
        for i, num in enumerate(nums):
            to_find = target - num
            index = mp.get(to_find, None)
            if index is not None:
                return index, i
            mp[num] = i
        return -1, -1