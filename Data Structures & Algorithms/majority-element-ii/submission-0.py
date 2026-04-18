class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        req = len(nums) // 3
        counts = Counter(nums)
        res = []
        for num, count in counts.items():
            if count > req:
                res.append(num)

        
        return res