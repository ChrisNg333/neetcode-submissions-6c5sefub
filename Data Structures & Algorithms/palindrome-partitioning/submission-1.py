class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #helper function
        def isValid(s:str) -> bool:
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        def backtrack(path, index):
            if index == len(s):
                res.append(path[:])
                return

            for i in range(index + 1,len(s) + 1):
                sub = s[index:i]
                if isValid(sub):
                    path.append(sub)
                    backtrack(path, i)
                    path.pop()

        backtrack([],0)

        return res