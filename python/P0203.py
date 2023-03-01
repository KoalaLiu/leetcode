#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    """Solution"""

    def removeElements(self, head, val):
        if not head:
            return None

        res = ListNode(-1, head)
        p = res

        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return res.next


def main():
    """main"""
    vec, k = [1, 1, 1, 1, 1], 1
    vec, k = [1, 2, 2, 1, 1, 3, 1, 1], 1
    vec, k = [2, 1], 1
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    lst_new = s.removeElements(lst, k)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()