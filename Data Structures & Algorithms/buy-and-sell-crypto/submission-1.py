class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l, r = 0 , 1
        profit = 0

        while r < len(p):
            if p[l] > p[r]:
                l = r
            profit = max(profit,p[r]- p[l])

            r += 1

        return profit


        