class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = Counter(s1)
        window = defaultdict(int)

        cur = 0       # curr valid until == need 

        l, r = 0, len(s1) - 1
        window = Counter(s2[l:r+1])
        while r < len(s2):
            if window == count1:
                return True
            else:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1
                r += 1
                if r < len(s2):
                    window[s2[r]] += 1
                
            
        return False

