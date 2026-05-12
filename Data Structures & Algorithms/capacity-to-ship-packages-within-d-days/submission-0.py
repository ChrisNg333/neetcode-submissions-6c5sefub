class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        def simulate(capacity) -> int:
            curr = 0
            day = 1
            for wgt in w:
                if curr + wgt > capacity:
                    day += 1
                    curr = 0
                curr += wgt
            return day

        l = max(w)
        r = sum(w)

        while l < r:
            m = (l+r) // 2
            if simulate(m) <= days:
                r = m
            else:
                l = m + 1
        
        return l
        
