# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Visit, Left, Right  
#Maintain: Previous, current, and right subtree root  
class Solution:
    prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        else:
            self.flatten(root.right)
            self.flatten(root.left) 

            root.right = self.prev
            root.left = None
            self.prev = root 