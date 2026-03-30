class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        uniq = set()
        l = 0 

        for r in range(len(s)):
            while s[r] in uniq:    #encouter a repeated c
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r]) 
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen 

        
