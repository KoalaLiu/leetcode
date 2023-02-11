# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        f1, f2 = 1, 2
        tmp = f1
        for i in range(3, n+1):
            tmp = f1
            f1 = f2
            f2 = tmp + f2

        return f2
