# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def append(self, lst, val):
        if lst is None:
            return ListNode(val)

        new_node = ListNode(val)
        lst.next = new_node
        return new_node
    
    def simple_add(self, a, b, cf):
        val = a + b + cf
        cf_new = val / 10

        return val % 10, cf_new

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = self.append(None, -1)
        trailer = header

        cf = 0
        while l1 is not None and l2 is not None:
            val, cf = self.simple_add(l1.val, l2.val, cf)
            trailer = self.append(trailer, val)

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            val, cf = self.simple_add(l1.val, 0, cf)
            trailer = self.append(trailer, val)

            l1 = l1.next

        while l2 is not None:
            val, cf = self.simple_add(l2.val, 0, cf)
            trailer = self.append(trailer, val)

            l2 = l2.next

        if cf != 0:
            trailer = self.append(trailer, cf)

        return header.next