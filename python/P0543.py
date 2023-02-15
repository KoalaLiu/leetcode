# 深度优先搜索的方式
# 最大直径的路径，还是需要经过根节点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 0

        if root.left is None:
            depth_left = 0
        else:
            depth_left = self.dfs(root.left) + 1

        if root.right is None:
            depth_right = 0
        else:
            depth_right = self.dfs(root.right) + 1

        self.max = max(self.max, depth_left + depth_right)
        return max(depth_left, depth_right)
