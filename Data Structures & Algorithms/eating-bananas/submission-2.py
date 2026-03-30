class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            
            #sampling 
            eatTime = 0
            for n in piles:
                eatTime += (n + k - 1) // k

            if eatTime <= h :
                res = k
                r = k - 1
            else:
                l = k + 1
 
        return res

        
        
