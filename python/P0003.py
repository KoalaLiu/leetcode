class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        d = dict()

        length = 0
        index = 0
        while index < len(s):
            ch = s[index]
            if ch in d:
                index = d[ch] + 1
                if length > max_length:
                    max_length = length

                d = dict()
                length = 0
                continue

            length += 1
            d[ch] = index
            index += 1

        return max([length, max_length])