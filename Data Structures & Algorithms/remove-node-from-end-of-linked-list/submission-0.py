# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #get the length
        leng = 0
        ptr = head
        while ptr:
            leng += 1
            ptr = ptr.next
        
        #move to the node 
        needed = leng - n
        ptr = head
        prev = None

        if needed == 0:
            return head.next
        while needed > 0:
            needed -= 1
            prev = ptr
            ptr = ptr.next
        
        #removing the node
        prev.next = ptr.next


        return head


