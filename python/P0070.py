# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        a, b, tmp = 1, 2, 0
        for i in range(3, n+1):
            tmp = a
            a = b
            b = tmp + b

        return b
