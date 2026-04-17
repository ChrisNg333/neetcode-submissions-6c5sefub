class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def explore(path,index):
            res.append(path[:])

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                explore(path,i+1)
                path.pop()      #backtrack



        explore([],0)
        return res
