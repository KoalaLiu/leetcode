#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @author: liuxiji
# @time: 2023/02/23 16:23:07

"""
 DESCRIPTION:
"""

import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    """Solution
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # res
        res_dummy = ListNode(-1)
        res_trailer = res_dummy

        # 双指针: slow -> head, fast
        slow = ListNode(-1000, head)
        fast = head

        while fast is not None:
            if (fast.val != slow.val and
                (fast.next is None or fast.next.val != fast.val)):
                res_trailer.next = fast
                res_trailer = res_trailer.next

            fast = fast.next
            slow = slow.next

        res_trailer.next = None
        return res_dummy.next
 

def main():
    """main"""
    vec = [-1, 0, 0, 0, 0, 0, 3, 3]
    # vec = [1]
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    lst_new = s.deleteDuplicates(lst)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()