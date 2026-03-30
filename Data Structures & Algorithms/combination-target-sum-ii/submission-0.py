class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def explorer (path, total, index):
            if total == target:
                res.append(path[:])
                return 
            
            if total > target:
                return 
            
            for i in range(index, len(nums)):
                #skipping s
                if i > index and nums[i - 1] == nums[i]:
                    continue

                path.append(nums[i])
                explorer(path, total + nums[i],i+1)
                path.pop() # backtrack
            

        explorer([], 0, 0)
        return res
