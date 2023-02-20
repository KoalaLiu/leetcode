#  pa=headA, pb=headB
# 要让pa和pb走的路径一样长。让pa和pb走的一样长，肯定会相交

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB

        while pa != pb:
            if pa is None:
                pa = headB
            else:
                pa = pa.next

            if pb is None:
                pb = headA
            else:
                pb = pb.next

        return pa