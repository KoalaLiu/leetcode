# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p_step, p_two_steps = head, head

        while True:
            if not p_step or not p_two_steps or not p_two_steps.next:
                return False

            p_step = p_step.next
            p_two_steps = p_two_steps.next.next

            if p_step == p_two_steps:    # 有环
                return True
