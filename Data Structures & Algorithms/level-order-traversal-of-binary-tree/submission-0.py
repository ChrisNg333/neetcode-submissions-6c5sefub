# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        count = 1   #store number of nodes each level

        while q:
            steps = count
            count = 0
            l = []  #reset the list
            for _ in range(steps):
                node = q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)
                    count += 1
                if node.right:
                    q.append(node.right)
                    count += 1
            
            ans.append(l[:])
        return ans
