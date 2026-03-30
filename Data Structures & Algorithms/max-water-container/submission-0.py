class Solution:
    def maxArea(self, h: List[int]) -> int:
        most = 0
        l, r = 0, len(h) - 1

        while l < r:
            most = max(min(h[l],h[r]) * (r-l),most)
            if h[l] < h[r]:
                l += 1
            elif h[l] >= h[r]:
                r -= 1

        return most