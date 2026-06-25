class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []       #minheap (closest distance)

        res = []
        for x, y in points:
            #calc distance
            dist = math.sqrt( (x**2) + (y**2) )

            heapq.heappush(heap, (dist, x, y))

        
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x,y])

        return res
