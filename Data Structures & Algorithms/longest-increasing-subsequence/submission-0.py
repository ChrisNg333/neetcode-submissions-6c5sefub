class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(1,len(nums)):      #loop backward
            l = i
            while l >= 0:
                if nums[l] < nums[i]:
                    dp[i] = max(dp[i],dp[l] + 1)
                l -= 1

        
        return max(dp)