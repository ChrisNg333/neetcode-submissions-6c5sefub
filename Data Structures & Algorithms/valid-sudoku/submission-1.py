class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if b[r][c] != ".":
                    curr_box = (r//3)*3+(c//3)
                    if b[r][c] in rows[r] or b[r][c] in cols[c] or b[r][c] in box[curr_box]:
                        return False
                    rows[r].add(b[r][c])
                    cols[c].add(b[r][c])
                    box[curr_box].add(b[r][c])
        
        return True
                    