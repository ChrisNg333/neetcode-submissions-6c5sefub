class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in s:        # this would eliminating extra lookup 
                leng = 0
                cur = num
                while cur in s: 
                    leng += 1
                    cur += 1
                
                res = max(res, leng)
                
        return res