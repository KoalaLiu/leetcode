#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @author: liuxiji
# @time: 2023/02/23 14:09:23

"""
 DESCRIPTION:
"""

import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    """Solution
    """
    def swapPairs(self, head):
        """两两反转"""
        # 辅助链表
        # header, slow -> head, fast
        header = ListNode(-1, head)
        slow, fast = header, head

        while fast is not None and fast.next is not None:
            # 反转 fast & fast.next, slow为辅助
            tmp = fast.next
            slow.next = tmp
            fast.next = tmp.next
            tmp.next = fast

            # 反转前: slow -> fast -> fast.next
            # 反转后: slow -> fast.next -> fast
            # 下一步
            slow = fast
            fast = fast.next

        return header.next


def main():
    """main"""
    vec = [1, 2, 3, 4, 5, 6]
    # vec = [1]
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    lst_new = s.swapPairs(lst)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()