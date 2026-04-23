class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        lookup = set(nums)      #for faster lookup

        for num in nums:
            dummy = num 
            count = 1
            while dummy - 1 in lookup:
                dummy -= 1
                count += 1
            
            res = max(res, count)

        return res