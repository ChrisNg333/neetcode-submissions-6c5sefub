class Solution:
    def numRescueBoats(self, ppl: List[int], limit: int) -> int:
        if not limit or not ppl:
            return 0

        ppl = sorted(ppl)
        
        ans = 0
        l, r = 0, len(ppl) - 1

        while l <= r:
            remain = limit - ppl[r]
            r -= 1
            ans += 1
            if remain >= ppl[l]:
                l += 1


        return ans
            