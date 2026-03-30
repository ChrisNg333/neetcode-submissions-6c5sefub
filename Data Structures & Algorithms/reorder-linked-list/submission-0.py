# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1, p2 = head, head

        #divide the list into 2 parts
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        #reverse the 2nd part
        prev = None
        curr = p1.next

        p1.next = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        #merge the 2 linkedlist 
        p1 = head
        p2 = prev

        while p2:
            dummy1 = p1.next    #preserve next for list 1
            dummy2 = p2.next    #preserve next for list 2
            p1.next = p2
            p2.next = dummy1
            p1,p2 = dummy1, dummy2
            
        
            




        
