# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode(-1)
        list_index = header
        jw = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + jw
            jw = sum / 10

            list_index.next = ListNode(sum % 10)
            list_index = list_index.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = l1.val + jw
            jw = sum / 10

            list_index.next = ListNode(sum % 10)
            list_index = list_index.next
            l1 = l1.next

        while l2 is not None:
            sum = l2.val + jw
            jw = sum / 10

            list_index.next = ListNode(sum % 10)
            list_index = list_index.next
            l2 = l2.next
        
        if jw != 0:
            list_index.next = ListNode(jw)

        return header.next