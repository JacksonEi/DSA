# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root)!=-1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)
        if left_height==-1 or right_height==-1:
            return -1

        if abs(left_height-right_height)>1:
            return -1

        return 1+max(left_height,right_height)
        