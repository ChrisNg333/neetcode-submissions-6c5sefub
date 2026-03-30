# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        p1, p2 = l1, l2

        dummy = ListNode()
        curr = dummy

        while p1 or p2 or carry:                
            num1 = p1.val if p1 else 0
            num2 = p2.val if p2 else 0

            num = num1 + num2 + carry
            carry = 1 if num >= 10 else 0 

            curr.next = ListNode(num % 10)
            curr = curr.next

            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2
            

        return dummy.next





            


        