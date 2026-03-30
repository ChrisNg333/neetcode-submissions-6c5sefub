# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []

        #init first node each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,i,node))

        head = ListNode(0)
        cur = head  #pointer to the head

        while heap:
            val,i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next 

            if node.next:
                heapq.heappush(heap, (node.next.val,i, node.next))
                      

        return head.next