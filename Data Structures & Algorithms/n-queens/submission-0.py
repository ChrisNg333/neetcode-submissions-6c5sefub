class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        col = set()
        posDiag = set()     # (r + c)
        negDiag = set()     # (r - c)

        ans = []
        def explore(r):
            if r == n:
                ans.append([''.join(row) for row in board])
                return 

            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
            
                board[r][c] = 'Q'
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                explore(r + 1)
                
                board[r][c] = '.'
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)

            
        explore(0)

        return ans

