class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False]*len(nums)

        def explore(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i-1] == nums[i] and used[i-1] == False:
                    continue

                path.append(nums[i])
                used[i] = True


                explore(path)

                path.pop()
                used[i] = False

        explore([])

        return res