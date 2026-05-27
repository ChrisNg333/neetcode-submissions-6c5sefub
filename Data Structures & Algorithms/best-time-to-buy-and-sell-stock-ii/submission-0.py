class Solution:
    def maxProfit(self, p: List[int]) -> int:
        profit = 0 

        for i in range(1, len (p)):
            if p[i-1] < p[i] :
                diff = p[i] - p[i-1]
                profit += diff

        return profit 