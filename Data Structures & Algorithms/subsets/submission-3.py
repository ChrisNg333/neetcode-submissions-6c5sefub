class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        def explore(path, index):
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                explore(path, i + 1)
                path.pop()      #backtrack
    
        explore([],0)

        return res