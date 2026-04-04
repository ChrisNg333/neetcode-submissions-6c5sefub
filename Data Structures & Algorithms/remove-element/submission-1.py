class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        ptr = 0

        while ptr < len(nums):
            if nums[ptr] != val:
                ptr += 1
            else:
                nums.remove(nums[ptr])

        return len(nums)