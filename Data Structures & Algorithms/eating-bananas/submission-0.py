class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r)//2
            #potential testing
            total = 0 
            for n in piles:
                total += (n + k - 1) // k 
                      
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
                

        return res

        
        
