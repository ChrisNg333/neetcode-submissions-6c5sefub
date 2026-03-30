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
        old = {}
        
        cur = head

        while cur:
            dummy = Node(cur.val)
            old[cur] = dummy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old[cur]
            copy.next = old.get(cur.next)
            copy.random = old.get(cur.random)
            cur = cur.next

        return  old[head]
        
            