class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def explorer (path, total,index):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return 

            for i in range(index, len(nums)):
                path.append(nums[i])
                explorer(path, total + nums[i],i )
                path.pop() # remove the last element just added (backtrack)


        explorer([], 0, 0)

        return res

