class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        most = 0
        while l < r:
            water = (r - l) * min (h[r], h[l])
            most = max(most, water)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        return most
        

        