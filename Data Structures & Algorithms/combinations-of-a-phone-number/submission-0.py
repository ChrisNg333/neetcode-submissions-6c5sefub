class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        maps = {'2':"abc", '3': "def", '4':"ghi", '5':"jkl", '6':"mno",'7':"pqrs", '8':"tuv", '9':"wxyz"}
        ans = []
        def explore(path, i):
            if len(path) == len(digits):
                ans.append(path)
                return 
            
            for letter in maps[digits[i]]:
                explore(path + letter, i + 1)


        explore("", 0)
        return ans
