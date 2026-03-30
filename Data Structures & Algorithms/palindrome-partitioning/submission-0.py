class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        parts = []

        def dfs(i):
            if i >= len(s):
                ans.append(parts[:])

            for j in range(i, len(s)):
                if isPalin(s, i, j):
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop() #backtrack

                
        def isPalin(s, l , r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -= 1
            return True

        dfs(0)                
        return ans