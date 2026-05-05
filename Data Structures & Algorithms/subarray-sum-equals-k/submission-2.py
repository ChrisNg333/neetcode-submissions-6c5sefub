class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        prefx = defaultdict(int)    # store {sum : counts}
        prefx[0] = 1
        curr = 0     #current sum 
        res = 0     #count

        for n in nums:
            curr += n
            if (curr - k) in prefx:              # match found
                res += prefx[curr-k]
            
            prefx[curr] += 1       #store counts


        return res



