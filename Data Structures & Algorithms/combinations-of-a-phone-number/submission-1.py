class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char = {'2':"abc", '3':"def", '4':"ghi",'5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        if not digits:
            return []
        res = []

        def explore(path, index):
            if index == len(digits):        #qualified
                res.append(path)
                return
            
            for ch in num_char[digits[index]]:
                explore(path + ch, index + 1)
                #since using str(immutable) so no need to backtrack (or cleanup)

        explore("",0)
        return res
