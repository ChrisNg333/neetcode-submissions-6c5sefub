class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2,len(nums)):
            cur = nums[i] + dp[i-2]
            dp[i] = max(cur, dp[i-1])

        return max(dp)