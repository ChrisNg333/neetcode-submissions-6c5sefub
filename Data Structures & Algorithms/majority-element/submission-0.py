class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        curr = float('-inf')
        for num, count in counts.items():
            if count > curr:
                curr = count
                res = num



        return res


