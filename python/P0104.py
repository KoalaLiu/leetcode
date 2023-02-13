# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node: TreeNode) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return 1 + max(self.depth(node.left), self.depth(node.right))


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
