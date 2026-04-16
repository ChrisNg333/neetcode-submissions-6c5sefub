class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def explore(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue        # to skip current number
                path.append(num)
                explore(path)
                path.pop() #backtrack 

        explore([])
        return res 