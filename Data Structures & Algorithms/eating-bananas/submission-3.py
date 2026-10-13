class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        r = max(piles)
        l = 1
        
        while l < r:
            mid = (l+r) // 2       #rate
            time = 0       #time needed
            for p in piles:
                time += math.ceil(p/mid)

            if time <= h:       #within range, so try smaller k
                r = mid 
            else:       #time <= h
                l = mid + 1


        return l
            