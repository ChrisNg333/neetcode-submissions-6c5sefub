class Solution:
    def maxArea(self, h: List[int]) -> int:
        most = 0 
        l , r = 0, len(h) - 1

        while l < r:        #no overlap
            area = min(h[l], h[r]) * (r-l)
            most = max(most, area)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        return most



        