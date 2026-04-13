class Solution:
    def findClosestElements(self, ar: List[int], k: int, x: int) -> List[int]:
        l , r = 0, len(ar) - k

        while l < r:
            mid = (l+r)//2

            if x - ar[mid] > ar[mid+k] - x:
                l = mid + 1

            else:
                r = mid 

        return ar[l:l+k]

        