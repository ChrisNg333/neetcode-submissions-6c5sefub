class Solution:
    def trap(self, h: List[int]) -> int:
        #2 pass approach for max prefix and max suffix 
        n = len(h)
        pref = [h[0]] * n  #max from left 
        suff = [h[n-1]] * n  # max from right 

        curr = h[0]
        for i in range(1,n):    
            pref[i] = max(curr, h[i])
            curr = pref[i]
        curr = h[-1]
        for i in range(n-2, -1, -1):    
            suff[i] = max(curr, h[i])
            curr = suff[i]
        #print(pref)
        #print(suff)
        # calc
        water = 0
        for i in range(n):
            water += (min(pref[i], suff[i]) - h[i])

        return water 




