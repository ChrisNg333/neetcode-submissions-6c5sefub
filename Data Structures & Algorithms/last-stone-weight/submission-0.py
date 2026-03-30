class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]

        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)

            heapq.heappush(maxheap, -abs(stone1 - stone2))

        return -maxheap[0]

