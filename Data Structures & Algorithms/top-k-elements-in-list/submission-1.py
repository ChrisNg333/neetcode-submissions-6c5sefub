class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        maxheap = [(-freq,num) for num,freq in count.items()]
        heapq.heapify(maxheap)
        ans = []

        for _ in range(k):
            freq,num = heapq.heappop(maxheap)
            ans.append(num)

        return ans

        