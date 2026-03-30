class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        lookup = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in lookup:     #if its the start of seq
                num = n
                seq = 1
                while num + 1 in lookup:
                    seq += 1
                    num += 1
                res = max(res, seq)  
        

        return res