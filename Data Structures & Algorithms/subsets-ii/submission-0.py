class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def explore(path, idx):    
            res.append(path[:])
            
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                explore(path,i + 1)
                path.pop()#backtrack
        

        explore([],0)
        return res


        