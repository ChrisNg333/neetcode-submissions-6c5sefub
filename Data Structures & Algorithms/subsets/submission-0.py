class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []

        def explore(path, start):
            ans.append(path[:])

            for i in range (start, len(nums)):
                path.append(nums[i])            #add num into path 
                explore(path, i + 1) #then explore with new element    
                path.pop() # then backtrack



        explore ([], 0)
        return ans