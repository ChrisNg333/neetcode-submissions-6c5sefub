class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        maxheap = [(-freq, num) for num, freq in counts.items()]       # store [num, freq]
        heapq.heapify(maxheap)
        res = []
        for _ in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)
        

        return res