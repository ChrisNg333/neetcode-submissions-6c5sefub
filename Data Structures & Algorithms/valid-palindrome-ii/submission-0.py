class Solution:
    def validPalindrome(self, s: str) -> bool:
        #helper function
        def isValid(l, r) -> bool:
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:    #mismatch occur
                return isValid(l, r -1) or isValid(l+1, r)         
            l += 1
            r -= 1

        return True