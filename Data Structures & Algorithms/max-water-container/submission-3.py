class Solution:
    def maxArea(self, h: List[int]) -> int:
        """
        approach:
        - prioritize higher bar, so move the short one 
        """
        if not h:
            return 0

        l,r = 0, len(h) - 1
        water = float('-inf')

        while l < r:
            width = r - l
            water = max(water, width*min(h[l], h[r]))

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        return water
