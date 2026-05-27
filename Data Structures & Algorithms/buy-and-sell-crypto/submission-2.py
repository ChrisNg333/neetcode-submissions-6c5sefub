class Solution:
    def maxProfit(self, prc: List[int]) -> int:
        profit = 0
        l ,r = 0, 1

        while r < len(prc):
            if prc[r] < prc[l]:
                l = r
            profit = max(profit, prc[r] - prc[l])
            r += 1
            

        return profit