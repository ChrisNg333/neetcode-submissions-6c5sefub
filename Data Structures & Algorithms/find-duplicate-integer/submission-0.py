class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()

        for num in nums:
            if num in uniq:
                return num

            uniq.add(num)    
            
        

