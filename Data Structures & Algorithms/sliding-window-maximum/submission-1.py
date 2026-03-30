class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [0]
        if k >= len(nums):
            return [max(nums)]
        l = 0 #leftbound
        ans = []    #container for ans
        q = deque()

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < nums[i]:
                q.pop() #remove the last element since they cant be max

            q.append(i) #this would be a new max

            #if front index is out of window, pop left
            while q and q[0] < l:
                q.popleft()
        
            if (i-l+1) == k:
                ans.append(nums[q[0]])
                l += 1
        
        return ans







