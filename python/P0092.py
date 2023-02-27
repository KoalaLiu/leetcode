#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:92
"""


import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return head

        # 构建辅助node: subslow -> slow -> fast, head -> RestOfList
        fast = head
        slow = ListNode(-65535, fast)
        dummy = slow

        # slow在right的位置，fast=slow.next
        # head -> xxx -> rigth, slow -> fast -> RestOfList
        subslow = None
        for _ in range(left):
            subslow = slow
            fast = fast.next
            slow = slow.next
        # print(subslow.val)

        # 翻转list
        for _ in range(right - left):
            tmp = fast
            fast = fast.next
            tmp.next = slow
            slow = tmp

        # print(slow.val, fast.val)

        tmp = subslow.next
        # print(tmp.val)
        subslow.next = slow
        tmp.next = fast

        return dummy.next


def main():
    """main"""
    vec = [1,2,3,4,5]
    left, right = 1, 5
    # vec = [5]
    # left, right = 1, 1

    vec = helper.build(vec)
    helper.debug_print(vec)

    s = Solution()
    r = s.reverseBetween(vec, left, right)
    helper.debug_print(r)


if __name__ == '__main__':
    main()