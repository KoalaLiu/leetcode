#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @author: liuxiji
# @time: 2023/02/22 16:41:44

"""
 DESCRIPTION: 用快慢指针
"""

class ListNode(object):
    """ Node
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 辅助node: header, fast, slow -> head
        header = ListNode(-1)
        header.next = head
        fast, slow = header, header

        # fast先走n步
        for _ in range(n):
            fast = fast.next

        # slow & fast走到最后
        # 最终node顺序: slow -> target(倒数第n个) -> 其他Nodes -> fast -> NULL
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow后面的节点需要删除
        tmp = slow.next
        slow.next = tmp.next
        tmp.next = None     # 置空：有助于垃圾回收？

        return header.next


def main():
    """main"""
    import LinkedListHelper as helper

    vec = [1, 2]
    n = 2
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    lst_new = s.removeNthFromEnd(lst, n)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()