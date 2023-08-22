# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        self.path_sum = float('-inf')  
        def dfs(root):
            if not root:
                return 0 
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.path_sum = max(self.path_sum, left + right + root.val)
            return max(left, right) + root.val
        dfs(root)
        return self.path_sum