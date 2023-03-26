# 二叉树后序遍历
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = deque()

        stack.append(root)
        while stack:
            top = stack.pop()
            if top:
                stack.append(top)
                stack.append(None)
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
            else:
                top = stack.pop()
                res.append(top.val)

        return res
