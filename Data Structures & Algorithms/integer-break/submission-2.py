class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n <= 3:
            return n - 1
        
        time3 = n // 3      #how many 3 
        remain = n % 3

        if remain == 0:     #perfect case
            return 3**time3
        elif remain == 2:       #keep it 
            return ((3**time3) * 2)
        elif remain == 1:
            time3 -= 1
            return (3**time3)*4





        
