class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        s = set(nums)

        for num in nums:
            leng = 1
            while num + 1 in s:
                leng += 1 
                num += 1
            else:
                res = max(res, leng)
            

        return res