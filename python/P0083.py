# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        trailer = dummy

        while head:
            if not head.next or head.val != head.next.val:
                trailer.next = head
                trailer = trailer.next

            head = head.next

        return dummy.next