class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0 
        lookup = set(nums)

        for n in nums:
            #look for the head
            while n-1 in lookup:
                n -= 1
            count = 1 
            while n + 1 in lookup:
                count += 1
                n += 1
            maxCount = max(maxCount, count)

        return maxCount