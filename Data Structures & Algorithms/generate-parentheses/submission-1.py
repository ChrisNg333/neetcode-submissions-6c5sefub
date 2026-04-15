class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def explore(path, left, right):
            if len(path) == n*2:
                res.append(path)
                return 
            
            if right > left:
                explore(path+')', left, right - 1)
            if left > 0 :
                explore(path + '(', left - 1, right)
            
          
                
            

        explore("",n,n)
        return res