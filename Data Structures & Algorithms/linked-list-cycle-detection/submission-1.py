# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ahead, here = head, head

        while ahead and ahead.next:
            ahead = ahead.next.next
            here = here.next

            if here == ahead:
                return True
        
        return False


            

            