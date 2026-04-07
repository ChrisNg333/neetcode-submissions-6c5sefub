class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def explore(path, index):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(index,n+1):
                path.append(i)
                explore(path, i + 1)
                path.pop()      #backtrack
        
        explore([],1)

        return res