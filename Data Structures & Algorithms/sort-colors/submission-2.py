class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1 # l for 0, r for 2
        pt = 0  

        while pt <= r:
            if nums[pt] == 0:   #swap with l
                nums[pt], nums[l] = nums[l], nums[pt]
                l += 1
                pt += 1
            
            elif nums[pt] == 2: #swap with r
                nums[pt], nums[r] = nums[r], nums[pt]
                r -= 1

            else:       #if 1
                pt += 1

            
            

        
                
            
            