# 二叉树中序遍历

from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = deque()

        # 左链入栈
        p = root
        while p:
            stack.append(p)
            p = p.left

        # 遍历栈
        while stack:
            top = stack.pop()
            res.append(top.val)

            # top的右孩子，继续左链入栈
            p = top.right
            while p:
                stack.append(p)
                p = p.left

        return res

    def inorderTraversal3(self, root):
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
                if top.right:
                    stack.append(top.right)
                stack.append(top)
                stack.append(None)
                if top.left:
                    stack.append(top.left)
            else:
                top = stack.pop()
                res.append(top.val)

        return res
