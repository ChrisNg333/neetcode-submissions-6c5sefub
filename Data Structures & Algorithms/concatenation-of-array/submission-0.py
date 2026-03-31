class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]*(2*len(nums))

        for i in range(len(res)):
            a = i % len(nums)
            res[i] = nums[a]


        return res