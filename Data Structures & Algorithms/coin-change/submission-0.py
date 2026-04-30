class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                remain = i - coin
                if remain >= 0:
                    dp[i] = min(dp[remain]+1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1