class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        n = len(nums)
        def explore(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] not in path:
                    #visited.add(nums[i])
                    path.append(nums[i])
                    explore(path)
                    #visited.remove(nums[i]) # backtrack
                    path.pop()
                     

        explore([])
        return res