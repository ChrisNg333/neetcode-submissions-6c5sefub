class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def explore(i, r, c) -> bool:
            if i == len(word):
                return True
            
            # fail condition:
            if (
                r >= rows or r < 0 or 
                c >= cols or c < 0 or 
                (r,c) in visited or 
                board[r][c] != word[i]
            ):
                return False

            visited.add((r,c))

            res = (
                explore(i + 1, r-1, c) or
                explore(i + 1, r, c-1) or 
                explore(i + 1, r+1, c) or 
                explore(i + 1, r, c+1)
            )         

            visited.remove((r,c))

            return res
            


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:      #1st char checkout 
                    if explore(0, r,c):
                        return True
        
        return False

            





