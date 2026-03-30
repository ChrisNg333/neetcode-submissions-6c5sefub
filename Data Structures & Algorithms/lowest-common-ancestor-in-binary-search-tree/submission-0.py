# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root :
            return None

        while root:
            if p.val < root.val and q.val < root.val:   #both value on the left
                root = root.left

            elif p.val > root.val and q.val > root.val: #both value on right 
                root = root.right
            
            else:
                return root 

            






