class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        part = [0] * k

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        if nums[0] > target:
            return False

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if part[j] + nums[i] <= target:
                    part[j] += nums[i]

                    if dfs(i + 1):
                        return True
                    
                    part[j] -= nums[i]

                    #optimization
                    if part[j] == 0:
                        break
            return False 
        return dfs(0)
