# 判断二叉树是否对称
# TODO 非递归的方法

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def cmp(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None and node2 is None:  # 根节点
            return True
        if node1 is None or node2 is None or node1.val != node2.val:    # 普通节点不对称的情况
            return False

        return self.cmp(node1.left, node2.right) and self.cmp(node1.right, node2.left)   # 遍历 右子右&左子左 和 右子左&左子右 是否对称


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.cmp(root.left, root.right)