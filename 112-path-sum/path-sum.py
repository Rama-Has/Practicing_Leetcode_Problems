# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, target):
            if not root:
                return False
            else:
                if target == root.val and not root.right and not root.left:
                    return True
                right_path_sum = dfs(root.right, target - root.val)
                left_path_sum = dfs(root.left, target - root.val)
                return right_path_sum or left_path_sum

        return dfs(root, targetSum)

