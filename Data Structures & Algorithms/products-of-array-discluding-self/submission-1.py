class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        res = [1]*len(nums)
        #1st pass
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]

        #2nd pass
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]      # multiply with prev element
        
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums)-1 else 1
            res[i] = left * right

        return res
            