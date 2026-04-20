class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        k = 0
        i = 0       #pointer 
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                nums.remove(nums[i])
            else:
                i += 1
                k += 1

        return k