# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        heap = []       #minheap

        #append the head into min heap
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,i,node))
                
        #reconstructing the list
        while heap:
            _, i ,node= heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val,i,node.next))
            curr.next = node
            curr = curr.next 


        return dummy.next
