#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @author: liuxiji
# @time: 2023/02/22 17:17:43

"""
 DESCRIPTION:
"""

import LinkedListHelper as helper


class ListNode(object):
    """ Node
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swap_helper(self, n1, n2):
        """ 交换n1.next 和 n2
            node顺序: n1 -> n1_next -> n2
            交换后: n1 -> n2 -> n1_next

            before: n1, n2 = slow, fast
            after: n1, tmp = slow, fast
        """
        tmp = n1.next
        n1.next = n2
        tmp.next = n2.next
        n2.next = tmp

        return n1, tmp

    def swapPairs_ugly(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        slow = ListNode(-1)
        slow.next = head
        fast = head.next
        res = fast

        slow, fast = self.swap_helper(slow, fast)
        # res = slow.next

        # print(slow.val, fast.val, res.val)
        # helper.debug_print(res)

        step = 0
        while fast.next is not None:
            step += 1
            slow = slow.next
            fast = fast.next

            if step >= 2:
                step = 0
                slow, fast = self.swap_helper(slow, fast)
                # print(slow.val, fast.val, fast.next.val)

        return res

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        # 辅助node: slow->head->fast
        # res = fast
        slow = ListNode(-1)
        slow.next = head
        fast = head.next
        res = fast

        step = 2
        while fast.next is not None:
            if step >= 2:    # 每走2步，进行一次swap
                step = 0
                slow, fast = self.swap_helper(slow, fast)

            step += 1
            slow = slow.next
            fast = fast.next

        if step >= 2:
            self.swap_helper(slow, fast)

        return res


def main():
    """main"""
    vec = [1, 2, 3, 4, 5, 6]
    # vec = [1]
    lst = helper.build(vec)
    helper.debug_print(lst)

    s = Solution()
    # lst_new = s.swapPairs_ugly(lst)
    lst_new = s.swapPairs(lst)
    helper.debug_print(lst_new)


if __name__ == '__main__':
    main()