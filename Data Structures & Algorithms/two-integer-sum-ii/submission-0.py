class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l < r:
            num = nums[l] + nums[r]
            if num == target:
                return [l+1,r+1]
            elif num > target:
                r -= 1
            elif num < target:
                l += 1
