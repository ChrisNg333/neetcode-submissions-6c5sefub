"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copier = {None:None}
        cur = head


        # 1st pass : put the copy version into the dict
        while cur:
            copy = Node(cur.val)
            copier[cur] = copy
            cur = cur.next

        cur = head
        #2nd pass : unpack and connect using the copier
        while cur:
            copy = copier[cur]
            copy.next = copier[cur.next]
            copy.random = copier[cur.random]
            cur = cur.next

        return copier[head]