class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def explore(path, cur, start):
            if cur == target:
                res.append(path[:])
                return
            
            if cur > target:
                return 

            for i in range(start,len(nums)):
                path.append(nums[i])

                explore(path,cur + nums[i], i)

                path.pop()          #backtrack


        explore([],0,0)
        return res

            

