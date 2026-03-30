class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_sum = sum(nums)
        normal = sum([i for i in range(len(nums)+1)])

        return normal - list_sum