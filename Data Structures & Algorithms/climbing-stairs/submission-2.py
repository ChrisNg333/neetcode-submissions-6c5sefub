class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        s = [0]*(n+1)
        s[1] = 1
        s[2] = 2
        
        for i in range(3,n+1):
            s[i] = s[i-2] + s[i-1]

        return s[n]