class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""


        need = Counter(t)       #how many char in t
        window = defaultdict(int)     # how many sofar

        req = len(need)     # how many req, dont change only use to compare to 
        have = 0        # how many we're having so far in numbers, change base on window 
        
        minlen = float('inf')
        left = 0       #keep track of window return 
        res = ""

        l = 0   
        for r in range(len(s)):
            #update window
            if s[r] in need:
                window[s[r]] += 1
                if window[s[r]] == need[s[r]]:        
                    have += 1
            
            #shrink window
            while have == req:
                #update if window smaller
                if (r-l+1) < minlen:
                    minlen = r - l + 1
                    left = l
                    res = s[left:r+1]

                #shrink
                if s[l] in need:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        have -= 1

                l += 1



        return res


    





        