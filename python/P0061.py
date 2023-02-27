#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION: 61
"""

import LinkedListHelper as helper
from LinkedListHelper import ListNode


class Solution(object):
    """Solution
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next is None:
            return head
        # 等价于: 将后面k个Node，放到前面
        # 利用快慢指针
        fast, slow = head, head

        # 让指针就位, 最终: head -> xxx -> slow -> newHead -> xxx -> fast -> None
        lst_len = 0
        pointer = head
        while pointer is not None:
            lst_len += 1
            pointer = pointer.next

        k = k % lst_len
        for _ in range(k):
            if fast.next is None:
                fast = head
            else:
                fast = fast.next

        # fast和slow重叠，直接返回head即可
        if fast == slow:
            return head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # head接到fast后面, slow做为最后一个node
        new_head = slow.next
        fast.next = head
        slow.next = None

        return new_head
 

def main():
    """main"""
    def test_case(s, vec, k):
        """test一个vector"""
        print("---------------------------------------")
        print("k =", k)
        lst = helper.build(vec)
        helper.debug_print(lst)

        lst_new = s.rotateRight(lst, k)
        helper.debug_print(lst_new)
        print("---------------------------------------")

    s = Solution()
    cases = [
        ([1, 2], 0),
        ([1, 2], 2001),
        ([1], 0),
        ([1,2,3,4,5], 2),
    ]
    for case in cases:
        vec, k = case
        test_case(s, vec, k)


if __name__ == '__main__':
    main()