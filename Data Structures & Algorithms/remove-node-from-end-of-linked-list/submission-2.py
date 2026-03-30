# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        # fast go 1st
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next;

        # both go now 
        while fast.next:
            fast = fast.next
            slow = slow.next

        # delete the node
        temp = slow.next.next
        slow.next = temp

        return head

