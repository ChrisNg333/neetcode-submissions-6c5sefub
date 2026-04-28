class StockSpanner:

    def __init__(self):
        self.dp = []       # store (price : span)
        self.span = 0

    def next(self, price: int) -> int:
        #if 1st element
        if not self.dp:
            self.span = 1
            self.dp.append((price , self.span))
            return 1
        else:   #additional element
            if price < self.dp[-1][0]:
                self.dp.append((price, 1))
                return 1
            else:
                i = len(self.dp) - 1
                step = 1
                
                while i >= 0 and price >= self.dp[i][0]:
                    step += self.dp[i][1] 
                    i = i - self.dp[i][1] 
                    

                self.dp.append((price, step))
                return step






# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)