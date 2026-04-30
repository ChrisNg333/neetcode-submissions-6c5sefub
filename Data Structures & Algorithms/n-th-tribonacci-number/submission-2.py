class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0]*38
        fib[0] = 0
        fib[1] = 1
        fib[2] = 1

        if n < 3:
            return fib[n]

        for i in range(3,n+1):
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3]

        return fib[n]
