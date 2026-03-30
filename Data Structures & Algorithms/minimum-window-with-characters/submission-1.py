class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s or not t:
            return ""
        
        freq = Counter(t)
        window_count = {}
        formed = 0 
        required = len(freq)

        min_len = float('inf')
        l, r = 0, 0
        ans = (0,0)

        while r < len(s):
            ch = s[r]
            window_count[ch] = window_count.get(ch,0) + 1 

            if ch in freq and window_count[ch] == freq[ch]:
                formed += 1
            
            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    ans = (l, r)
                
                # Pop from left of window
                leftchar = s[l]
                window_count[leftchar] -= 1

                if leftchar in freq and window_count[leftchar] < freq[leftchar]:
                    formed -= 1
                
                l += 1

            r += 1


        return s[ans[0]: ans[1]+1] if min_len != float('inf') else ""
        

            

