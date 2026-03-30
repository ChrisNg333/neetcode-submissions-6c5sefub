# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0 #start at root
        def dfs (curMax, node):
            nonlocal count
            if not node:
                return

            if node.val >= curMax:
                curMax = node.val
                count += 1
            
            if node.left:
                dfs(curMax, node.left)

            if node.right:
                dfs(curMax, node.right)
          
        dfs(root.val, root)


        return count





                


        