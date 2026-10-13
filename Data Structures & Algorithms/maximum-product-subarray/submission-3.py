class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = 1         #track curr max

        cur_min = 1         #track cur min incase it flips

        for num in nums:
            candidates = [num, cur_max*num, cur_min*num]
            cur_max = max(candidates)
            cur_min = min(candidates)

            res = max(res, cur_max)

        return res