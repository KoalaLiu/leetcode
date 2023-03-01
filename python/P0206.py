#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    """Solution"""
    def reverseList(self, head):
        if not head:
            return None

        # slow -> fast, head
        slow = ListNode(-1, head)
        fast = head

        while fast is not None:
            tmp = fast
            fast = fast.next
            tmp.next = slow
            slow = tmp

        head.next = None

        return slow


def main():
    """main"""
    vec = [1, 2, 3, 4, 5]
    vec = []
    vec = [1]
    vec = [1, 2, 3, 4]
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    lst_new = s.reverseList(lst)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()