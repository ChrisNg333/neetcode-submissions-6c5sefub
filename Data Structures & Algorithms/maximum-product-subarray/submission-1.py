class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            prev = cur_max

            cur_max = max(num, num*cur_max, num * cur_min)            
            cur_min = min(num, num*prev, num*cur_min)

            ans = max(ans, cur_max)


        return ans