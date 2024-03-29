from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderedTraversal2(self, root):
        """ 非递归
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = deque()
        stack.append(root)

        while stack:
            top = stack.pop()
            if not top:
                continue

            res.append(top.val)
            stack.append(top.right)
            stack.append(top.left)

        return res

    def preorderdTraversal3(self, root):
        """ 非递归（模板）
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = deque()

        stack.append(root)
        while stack:
            top = stack.pop()
            if top:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
                stack.append(top)
                stack.append(None)
            else:
                top = stack.pop()
                res.append(top.val)

        return res
