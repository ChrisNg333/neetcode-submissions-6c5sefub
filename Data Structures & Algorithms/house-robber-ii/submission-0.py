class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def findmax(ar) -> int:
            dp = [0]*len(ar)
            dp[0], dp[1] = ar[0], max(ar[0],ar[1])

            for i in range(2,len(ar)):
                cur = ar[i] + dp[i-2]
                dp[i] = max(cur, dp[i-1])

            return max(dp)

        profit1 = findmax(nums[:-1])
        profit2 = findmax(nums[1:])
       
        return max(profit1, profit2)


        



