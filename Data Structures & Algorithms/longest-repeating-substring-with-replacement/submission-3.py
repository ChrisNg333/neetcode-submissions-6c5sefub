class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        window = defaultdict(int)
        maxlen = 0
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            window[s[r]] += 1
            maxfreq = max(maxfreq, window[s[r]])
            
            #shrink
            if (r - l + 1) - maxfreq > k:       #if k reach
                window[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen