class Solution:
    def trap(self, h: List[int]) -> int:
        # water[i] = min(left, right) - current[i]
        # if water[i] <= 0 -> water[i] = 0      # no water retain 
        n = len(h)
        res = 0 
        
        left =  [0] * n     # max left
        right = [0] * n     # max right 

        left [0], right[-1] = h[0], h[-1]

        #l -> r
        for i in range(1,n):
            left[i] = max(h[i], left[i-1])
        
        # r -> l
        for i in range(n-2, -1, -1):
            right[i] = max(h[i], right[i+1])

        for i in range(1,n-1):
            water = min(left[i-1],right[i+1]) - h[i]
            if water > 0:
                res += water

        return res


