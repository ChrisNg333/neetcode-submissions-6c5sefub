class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0 , 10:0}

        for num in bills:
            if num == 5:
                change[5] += 1
            
            elif num == 10:
                if change[5] < 1:
                    return False
                change[10] += 1
                change[5] -= 1
            
            else:
                #try 10 + 5 fisrt 
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                
                #then do 5+5+5 later
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True

                
                
