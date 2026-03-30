# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare (root1, root2)-> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            if root1.val != root2.val: 
                return False         
            return compare(root1.left, root2.left) and compare(root1.right, root2.right)


        def isSame(root, sub)-> bool:
            if not root:
                return False
            
            if compare(root, sub):
                return True
            return isSame(root.left, sub) or isSame(root.right, sub)
        
        
        return isSame(root, subRoot)
        

