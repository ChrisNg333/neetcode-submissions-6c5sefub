class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numx = {num:i for i,num in enumerate(nums)}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in numx and numx[diff] != i:
                return [i, numx[diff]]