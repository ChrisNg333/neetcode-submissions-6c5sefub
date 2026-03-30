class Solution:
    def trap(self, h: List[int]) -> int:
        # water[i] = min(left, right) - height[i]
        n = len(h)
        # 1st pass
        maxleft = [0]*n
        maxleft[0] = h[0]
        for i in range(1, n):
            maxleft[i] = max(h[i], maxleft[i-1])

        # 2nd pass
        maxright = [0]*n
        maxright[n-1] = h[n-1]
        for i in range(n-2,-1,-1):
            maxright[i] = max(h[i], maxright[i+1])

        #3rd pass
        water = 0
        for i in range(n):
            water += min(maxleft[i], maxright[i]) - h[i]


        return water
