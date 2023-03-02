from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.que = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.que.append(t)

        k = 0
        for qt in self.que:
            if t - qt > 3000:   # 超过3000ms
                k += 1
            else:
                break

        for _ in range(k):
            self.que.popleft()

        return len(self.que)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)