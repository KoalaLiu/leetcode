# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        target = head   # 倒数第N个Node，倒数第N-1个Node
        target_pre = ListNode(-1, target)
        pre = target_pre

        steps = 0
        while head is not None:
            steps += 1

            if steps > n:
                target_pre = target
                target = target.next

            head = head.next
 
        target_pre.next = target.next
        target.next = None

        return pre.next


if __name__ == '__main__':
    def printList(lst):
        numbers = []
        while lst is not None:
            numbers.append(lst.val)
            lst = lst.next
        print(numbers)

    def append(node, val):
        if not node:
            return ListNode(val)
        node.next = ListNode(val)

        return node.next

    lst = [1, 2]
    n = 2

    header = append(None, -1)
    node = header
    for x in lst:
        node = append(node, x)

    lst = header.next
    printList(lst)

    s = Solution()
    newlst = s.removeNthFromEnd(lst, n)
    printList(newlst)
